from django.conf.urls import patterns, url

from Inventario.views import *

urlpatterns = patterns('',

    url(r'^reporteCompras/$', ComprasProveedor),
    url(r'^jsonCompras/$', ReporteCompra),

    url(r'^TemplatereporteFaltantes/$', TemplateReporteFaltantes),
    url(r'^reporteFaltantes/$', ReporteFaltantes),
    url(r'^conciliaInventario/$', ConciliaInventario),

    url(r'^TemplateMovimientos/$', TemplateMovimientos),
    url(r'^reporteMovimientos/$', ReporteMovimientos),

    url(r'^ajustes/$',GestionAjustes),
    url(r'^guardarAjustes/$',GuardarAjuste),
    url(r'^EditaAjustes/(?P<idAjuste>\d+)',EditarAjustes),


    url(r'^provedorAjax/$', listaProvedoresAjax),

    url(r'^listaProd/$', listaProductos),
    url(r'^consultaStock/$', consultaStock),
    #url(r'^verSubProductos/$',listaSubProductos),
    url(r'^bodega/$',GestionBodega),
    url(r'^provedor/$',GestionProvedor),
    url(r'^ganado/(?P<idcompra>\d+)',GestionGanado),

    url(r'^deshidratacion/$',Deshidratacion),

    url(r'^grupo/$',GestionGrupo),

    url(r'^recepcion/(?P<idcompra>\d+)',GestionPlanillaRecepcion),

    url(r'^traslado/$',GestionTraslados),
    url(r'^editaTraslado/(?P<idTraslado>\d+)',EditaTraslados),
    url(r'^EditaDetTraslado/(?P<idDettraslado>\d+)',EditaDetalleTraslado),
    url(r'^borrarTraslado/(?P<idTraslado>\d+)',borrarTraslado),
    url(r'^guardaTraslado/$',GuardarTraslado),
    url(r'^dettraslado/(?P<idtraslado>\d+)',GestionDetalleTraslado),
    url(r'^borraDetTraslado/(?P<idDetTraslado>\d+)',borrarDetTraslado),
    #url(r'^reporteTraslado/(?P<idTraslado>\d+)',ReporteTraslado),
    url(r'^compra/(?P<tipoCompra>\d+)',GestionCompra),
    url(r'^guardaCompra/$',GuardarDetCompra),
    url(r'^detcompra/(?P<idcompra>\d+)',GestionDetalleCompra),
    url(r'^editaDetCompra/(?P<idDetCompra>\d+)',EditaDetalleCompra),
    url(r'^borrarDetCompra/(?P<idDetCompra>\d+)',borrarDetCompra),
    url(r'^borrarCompra/(?P<idCompra>\d+)',borrarCompra),

    url(r'^editacompra/(?P<idDetCompra>\d+)',EditaCompra),
    url(r'^modifica/(?P<idCompra>\d+)',ModificaCompra),
    url(r'^productoBodega/(?P<idproducto>\d+)',GestionProductoBodega),
    #url(r'^addDSprod/(?P<id_subproducto>\d+)',AgregarDetSubProducto, name='gestionSp'),
    url(r'^borrar/(?P<id_producto>\d+)',borrar_producto),
    #url(r'^borrarSP/(?P<idSubproducto>\d+)',borrarSubproducto),
    #url(r'^borrardetSP/(?P<idDetalle>\d+)',borrarDetalleSp),
    url(r'^borrarBodega/(?P<idbodega>\d+)',borrarBodega),
    url(r'^editar/(?P<id_producto>\d+)',editar_producto),
    url(r'^editarBodega/(?P<idBodega>\d+)',editarBodega),
    #url(r'^editarSP/(?P<idSproducto>\d+)',editarSubproducto),
    url(r'^movimiento/$',GestionMovimientos),

    url(r'^faltante/$',GestionFaltante),
    url(r'^detalleFaltante/(?P<idFaltante>\d+)',GestionDetalleFaltante),
    url(r'^EditaFaltante/(?P<idDetFaltante>\d+)',EditaDetalleFaltante),
    url(r'^generarFaltante/$',GenerarFaltante),

    url(r'^cantidadActual/$',CantidadActual),


)
