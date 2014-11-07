from django.conf.urls import patterns, url

from Ventas.views import *


urlpatterns = patterns('',

    url(r'^ventas/$',GestionVentas),
    url(r'^detalleVentas/(?P<idVenta>\d+)',GestionDetalleVentas),
    url(r'^consultaPrecioProducto/$',consultaValorProducto),
    url(r'^guardaVenta/$',GuardarVenta),
    url(r'^consultaCosto/$',consultaCostoProducto),
    url(r'^editaDetVenta/(?P<idDetVenta>\d+)',EditaDetalleVentas),

    url(r'^pedido/(?P<idcliente>\d+)',GestionPedidos),
    url(r'^detallePedido/(?P<idpedido>\d+)',GestionDetallePedido),
    #url(r'^pedidoPdf/(?P<idpedido>\d+)',ReportePedido),
    url(r'^listaPrecios/$',GestionLista),
    url(r'^detalleLista/(?P<idLista>\d+)',GestionDetalleLista),
    url(r'^editaLista/(?P<idDetLista>\d+)',EditaListas),

    url(r'^ventaPunto/$',PuntoVenta),
    url(r'^detalleVentaPunto/(?P<idVenta>\d+)',DetallePuntoVenta),
    url(r'^editaVentaPunto/(?P<idDetVenta>\d+)',EditaPuntoVenta),
    url(r'^eliminaVentaPunto/(?P<idDetVenta>\d+)',EliminaPuntoVenta),
    url(r'^valorProdVenta/$',ValorProdVenta),

    url(r'^caja/$',GestionCaja),
    url(r'^editaCaja/(?P<idCaja>\d+)',EditaCaja),

    url(r'^cobrar/$',CobrarVenta),

)
