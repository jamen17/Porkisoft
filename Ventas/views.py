# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response,HttpResponseRedirect
from django.template import RequestContext
from Ventas.Forms import *
#Imports necesarios para el uso de Pisa PDF
import ho.pisa as pisa
import cStringIO as StringIO
import cgi

from decimal import Decimal

import json
from django.template.loader import render_to_string
from django.http import HttpResponse


def generar_pdf(html):
    # Función para generar el archivo PDF y devolverlo mediante HttpResponse
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), mimetype='application/pdf')
    return HttpResponse('Error al generar el PDF: %s' % cgi.escape(html))


def ReportePedido(request,idpedido):
   # vista de ejemplo con un hipotético modelo Libro
    detallePedido = DetallePedido.objects.filter(pedido = idpedido)
    pedido = Pedido.objects.get(pk = idpedido)

    html = render_to_string('Ventas/Pedido_pdf.html', {'pagesize':'A4', 'detallePedido':detallePedido,'pedido':pedido},
                            context_instance=RequestContext(request))
    return generar_pdf(html)


def GestionPedidos(request,idcliente):
    pedidos = Pedido.objects.filter(cliente = idcliente)
    cliente = Cliente.objects.get(pk = idcliente)
    if request.method =='POST':
        formulario = PedidoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/ventas/pedido/'+idcliente)
    else:
        formulario = PedidoForm(initial={'cliente':cliente})

    return render_to_response('Ventas/GestionPedido.html',{'formulario':formulario,'pedidos':pedidos,'cliente':cliente},
                              context_instance = RequestContext(request))

def GestionDetallePedido(request,idpedido):
    pedido = Pedido.objects.get(pk = idpedido)
    detPedido = DetallePedido.objects.filter(pedido = idpedido)
    vrPedido = 0

    for det in detPedido:
        vrPedido += det.vrTotal

    if request.method =='POST':
        formulario = DetallePedidoForm(request.POST)
        if formulario.is_valid():
            detalle = formulario.save()

            pedido.TotalVenta = vrPedido + detalle.vrTotal
            pedido.save()

            return HttpResponseRedirect('/ventas/detallePedido/'+idpedido)
    else:
        formulario = DetallePedidoForm(initial={'pedido':idpedido})

    return render_to_response('Ventas/GestionDetallePedido.html',{'idPedido':idpedido,'formulario':formulario,'pedido':pedido,
                                                                  'detPedido':detPedido,'vrPedido':vrPedido},
                              context_instance = RequestContext(request))

def GestionVentas(request):

    ventas = Venta.objects.all()

    if request.method =='POST':
        formulario = VentaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/ventas/ventas/')
    else:
        formulario = VentaForm()

    return render_to_response('Ventas/GestionVentas.html',{'formulario':formulario,'ventas':ventas},
                              context_instance = RequestContext(request))

def GestionDetalleVentas(request,idVenta):

    venta = Venta.objects.get(pk = idVenta)
    detalles = DetalleVenta.objects.filter(venta = idVenta)


    if request.method =='POST':
        formulario = VentaDetalleForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            #sumamos los valores de la venta
            vrTotalContado = 0
            vrTotalCredito = 0
            vrTotal = 0
            detalles = DetalleVenta.objects.filter(venta = idVenta)
            for det in detalles:
                if det.contado == True:
                    vrTotalContado += det.vrTotal
                elif det.credito == True:
                    vrTotalCredito += det.vrTotal
                vrTotal += det.vrTotal

            venta.TotalVenta = vrTotal
            venta.TotalCredito = vrTotalCredito
            venta.TotalContado = vrTotalContado
            venta.save()

            return HttpResponseRedirect('/ventas/detalleVentas/'+idVenta)
    else:
        formulario = VentaDetalleForm(initial={'venta':idVenta})

    return render_to_response('Ventas/GestionDetalleVentas.html',{'formulario':formulario,'venta':venta,'detalles':detalles},
                              context_instance = RequestContext(request))

def consultaValorProducto(request):
    idProducto = int(request.GET.get('idProducto'))
    idVenta = int(request.GET.get('idVenta'))
    peso = int(request.GET.get('peso'))

    venta = Venta.objects.get(pk = idVenta)
    producto = Producto.objects.get(pk = idProducto)

    #verificamos si el producto cuenta con esa cantidad en bodega
    bodega = ProductoBodega.objects.get(bodega = venta.bodega.codigoBodega,producto =producto.codigoProducto )

    if peso <= bodega.pesoProductoStock :
        vrProducto = producto.precioSugerido
        exito = vrProducto
    else:
        exito = False

    respuesta = json.dumps(exito)
    return HttpResponse(respuesta,mimetype='application/json')

def GuardarVenta(request):

    #Tomo los datos necesarios del request como son el id de la venta para ubtener los registros que quiero guardar
    idVenta = int(request.GET.get('idVenta'))
    peso = request.GET.get('peso')
    venta = Venta.objects.get(pk = idVenta)
    ventas = DetalleVenta.objects.filter(venta = idVenta)
    registros = ventas.count()

    #voy por todos los productos de esa venta para guardar restar cantidades uno a uno

    for vnt in ventas :
        bodega = ProductoBodega.objects.get(bodega = venta.bodega.codigoBodega,producto = vnt.producto.codigoProducto)
        bodega.pesoProductoStock -= Decimal(peso)
        bodega.save()

    msj = 'Se guardaron %d registros exitosamente'%registros
    respuesta = json.dumps(msj)
    return HttpResponse(respuesta,mimetype='application/json')

