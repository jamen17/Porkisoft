from django.conf.urls import patterns, url
from Fabricacion.views import *

urlpatterns = patterns('',
    # Examples:

    url(r'^existencias/$',existencias),
    url(r'^existenciasund/$',existenciasUnd),
    url(r'^guardaDescarne/$',GuardaDescarne),
    url(r'^traercosto/$',TraerCosto),
    url(r'^traercostopollo/$',TraerCostoPollo),
    url(r'^traercostoFilete/$',TraerCostoFilete),
    url(r'^costearTajado/$',costearTajado),
    url(r'^guardarTajado/$',GuardarTajado),
    url(r'^guardarCondimentado/$',GuardarCondimentado),
    url(r'^guardarEnsalinado/$',GuardaEnsalinado),
    url(r'^costearApanado/$',costeoApanado),
    url(r'^guardarApanado/$',GuardarApanado),
    url(r'^costearMolido/$',costeoMolido),
    url(r'^guardarMolido/$',GuardarMolido),

    url(r'^costearEmpaque/$',CostearEmpacado),
    url(r'^guardarEmpaque/$',GuardarEmpacado),
    url(r'^consultaCostoChuleta/$',ConsultaCostoChuleta),

    url(r'^condimentado/$',GestionCondimentado),

    url(r'^empacadoApanado/$',GestionEmpacadoApanados),
    url(r'^editaEmpacadoApanado/(?P<idEmpacado>\d+)',EditaEmpacadoApanados),

    url(r'^menudos/$',GestionMenudos),
    url(r'^guardarMenudo/$',GuardarMenudos),

    url(r'^fritos/$',GestionFrito),
    url(r'^costearFritos/$',CostearFrito),
    url(r'^guardarFritos/$',GuardarFrito),

    url(r'^ensBola/$',GestionEnsBola),
    url(r'^costearEnsBola/$',CostearEnsBola),
    url(r'^guardarEnsBola/$',GuardarEnsBola),
    url(r'^editaEnsBola/(?P<idEns>\d+)',EditaEnsBola),

    url(r'^carneCondimentada/$',GestionCarneCond),
    url(r'^costearCarneCond/$',CostearCarneCond),
    url(r'^guardarCarneCond/$',GuardarCarneCond),

    url(r'^croquetas/$',GestionCroqueta),

    url(r'^canalPendiente/$',InformeCanalesPendientes),
    url(r'^descarne/$',GestionDescarneCabeza),
    url(r'^costos/$',GestionValorCostos),
    url(r'^editacosto/(?P<idcosto>\d+)',EditaCostos),
    url(r'^editaensalinado/(?P<idEnsalinado>\d+)',EditaEnsalinado),

    url(r'^templateTraslado/$',TemplateTraslados),
    url(r'^reporteTraslado/$',ReporteTraslados),

    url(r'^templateTrasladoBodega/$',TemplateTrasladosBodega),
    url(r'^reporteTrasladoBodega/$',ReporteTrasladosBodega),

    url(r'^templateTalleresPuntos/$',TemplateTalleresPuntos),
    url(r'^reporteTallerPunto/$',ReporteTallerPunto),

    url(r'^templateUtilidad/$',TemplateUtilidadPorLote),
    url(r'^utilidadReses/$',ReporteUtilidadPorLote),

     url(r'^molida/$',GestionMolido),

    url(r'^canal/(?P<idrecepcion>\d+)',GestionCanal),
    url(r'^borrarCanal/(?P<idcanal>\d+)',BorrarCanal),

    url(r'^marcarcanal/(?P<idcanal>\d+)',MarcarCanalDesposte),

    url(r'^desposte/$',GestionDesposte),
    url(r'^templateListDesp/$',TemplateListaDesposte),
    url(r'^reporteListDesp/$',ReporteListaDesposte),

    url(r'^sacrificio/(?P<idrecepcion>\d+)',GestionSacrificio),

    url(r'^detalleDesposte/(?P<idplanilla>\d+)',GestionDesposteActualizado),
    url(r'^costeoDesposte/$',costeoDesposte),
    url(r'^guardarDesposte/$',GuardarDesposte),
    url(r'^editaDesposte/(?P<idDetalle>\d+)',EditaDetPlanilla),

    url(r'^costearCroquetas/$',CostearCroqueta),
    url(r'^guardarCroquetas/$',GuardarCroqueta),

    url(r'^guardarMiga/$',GuardarMiga),

    url(r'^tallerReApanado/$',GestionReApanado),
    url(r'^guardarReApanado/$',GuardarReApanado),


    url(r'^conversiones/$',GestionConversiones),
    url(r'^Guardaconversiones/$',GuardarConversion),

    url(r'^chicharrones/$',GestionChicharron),
    url(r'^costearChicharrones/$',CostearChicharoones),
    url(r'^guardarChicharrones/$',GuardarChicharron),


    #url(r'^detalleDesposte/(?P<idplanilla>\d+)',GestionCanalDetalleDesposte),
    #url(r'^costoDesposte/(?P<idplanilla>\d+)',CostoDesposte),

    url(r'^ensalinados/$', GestionEnsalinado),

    url(r'^tajado/$', GestionTajado),
    url(r'^editaTajado/(?P<idTajado>\d+)',EditaTajado),

    url(r'^detalleTajado/(?P<idTajado>\d+)', GestionDetalleTajado),
    url(r'^editadetalleTajado/(?P<idDetTajado>\d+)', EditaDetalleTajado),
    url(r'^verduras/$', GestionVerduras),
    url(r'^condimento/$', GestionCondimento),
    url(r'^detallecondimento/(?P<idcondimento>\d+)', GestionDetalleCondimento),
    url(r'^costoCond/(?P<idcondimento>\d+)',CostoCondimento),
    url(r'^miga/$', GestionMiga),
    url(r'^detallemiga/(?P<idmiga>\d+)', GestionDetalleMiga),
    url(r'^costoMiga/(?P<idmiga>\d+)',CostoMiga),
    url(r'^apanados/$',GestionApanado),
    url(r'^editaApanados/(?P<idApanado>\d+)',EditaApanado),
    url(r'^promedio/$',promedioCostoProducto),
    url(r'^calcPromedio/$',CalcularPromedio),
    url(r'^TemplateCondPo/$',TemplatePromedioPechugaCond),
    url(r'^promPechCondPo/$',RepFiletePechugaCond),
    url(r'^TemplateInsumos/$',TemplateInsumos),
    url(r'^promInsumos/$',ReporteInsumos),
    url(r'^TemplateDescarnes/$',TemplateDescrnes),
    url(r'^promDescarnes/$',ReporteDescarnes),
    url(r'^editaDes/(?P<idDesposte>\d+)',EditaDesposte),



)
