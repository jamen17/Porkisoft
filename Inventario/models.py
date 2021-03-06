from django.db import models

# Create your models here.

class Grupo(models.Model):
    nombreGrupo = models.CharField(verbose_name='Nombre', max_length=20)
    refrigerado = models.BooleanField(verbose_name = 'Refrigerado')
    congelado = models.BooleanField(verbose_name = 'Congelado')

    def __unicode__(self):
        return self.nombreGrupo

class Bodega(models.Model):
    codigoBodega = models.AutoField(primary_key=True, verbose_name='Codigo Bodega')
    nombreBodega = models.CharField(max_length=50, verbose_name='Nombre')
    direccionBodega = models.CharField(max_length=50, verbose_name='Direccion')
    telefonoBodega = models.CharField(max_length=10,verbose_name='Telefono')
    activo = models.BooleanField(default=True)
    def __unicode__(self):
        return self.nombreBodega

class Producto(models.Model):

    codigoProducto = models.AutoField(primary_key=True, verbose_name='Codigo Producto')
    grupo = models.ForeignKey(Grupo)
    numeroProducto = models.BigIntegerField(verbose_name='Numero')
    nombreProducto = models.CharField(verbose_name = 'Nombre Producto',max_length=50)
    costoProducto = models.BigIntegerField(verbose_name = 'Costo Producto', default=0)
    precioSugerido = models.IntegerField(verbose_name='Precio Sugerido', default=0)
    gravado = models.BooleanField(verbose_name = 'Gravado 1', default=False)
    gravado2 = models.BooleanField(verbose_name = 'Gravado 2', default=False)
    excento = models.BooleanField(verbose_name='Excento',default=False)
    excluido = models.BooleanField(verbose_name='Excluido',default=False)
    pesables = models.BooleanField(verbose_name='Pesables',default=False)
    noPesables = models.BooleanField(verbose_name='No Pesables',default=False)


    def __unicode__(self):
        cadena = '%d ,%s , (%s)'%(self.numeroProducto,self.nombreProducto,self.grupo.nombreGrupo)
        return cadena

    class Meta:
        ordering = ['numeroProducto']



class SubProducto(models.Model):
    codigoSubProducto= models.AutoField(verbose_name='Codigo', primary_key=True)
    nombreSubProducto = models.CharField(verbose_name = 'Nombre',max_length=50)
    costoSubProducto = models.IntegerField(verbose_name = 'Costo')
    vrVentaSubProducto = models.IntegerField(verbose_name = 'Vr. Venta')
    utilidadSubProducto = models.IntegerField(verbose_name = 'Ulilidad')
    rentabilidadSubProducto = models.DecimalField(verbose_name = 'Rentabilidad',max_digits=5, decimal_places=2 )
    gravado = models.BooleanField(verbose_name = 'Gravado')
    excento = models.BooleanField(verbose_name='Excento')
    excluido = models.BooleanField(verbose_name='Excluido')
    refrigerado = models.BooleanField(verbose_name = 'Refrigerado')
    congelado = models.BooleanField(verbose_name = 'Congelado')


    def __unicode__(self):
        return self.nombreSubProducto

class DetalleSubProducto(models.Model):
    subproducto = models.ForeignKey(SubProducto)
    producto = models.ForeignKey(Producto, verbose_name='Producto')
    pesoUnitProducto = models.DecimalField(verbose_name = 'Peso Producto (grs)',max_digits=9, decimal_places=3,null= True,default=0)
    unidades = models.IntegerField(verbose_name='Unidades', null= True,default=0)

class ProductoBodega(models.Model):
    producto = models.ForeignKey(Producto)
    grupoProducto = models.CharField(blank=True,max_length=100)
    nombreProducto = models.CharField(blank=True,max_length=100)
    bodega = models.ForeignKey(Bodega)
    pesoProductoStock = models.DecimalField(max_digits=15,decimal_places=2,verbose_name='Peso en  Stock', default=0)
    pesoProductoKilos = models.IntegerField(verbose_name='Peso en  Stock(Kls)', default=0)
    unidadesStock = models.IntegerField(verbose_name='Unidades en Stock', default=0)
    #deshidratacion = models.DecimalField(max_digits=15, decimal_places=3,verbose_name='% Deshidratacion')

class SubProductoBodega(models.Model):
    subProducto = models.ForeignKey(SubProducto)
    bodega = models.ForeignKey(Bodega)
    pesoSubProductoStock = models.DecimalField(max_digits=9,decimal_places=2,verbose_name='Peso en  Stock')

class Traslado(models.Model):

    OpEstTraslado = (
    ('Enviado', 'Enviado'),
    ('Recibido', 'Recibido'),
    )


    codigoTraslado = models.AutoField(verbose_name='Codigo Traslado', primary_key=True)
    bodegaActual = models.ForeignKey(Bodega)
    bodegaDestino = models.CharField(max_length=20,verbose_name='Bodega Destino')
    #empleado = models.ForeignKey(Empleado)
    fechaTraslado = models.DateField(verbose_name='Fecha')
    estadoTraslado = models.CharField(verbose_name='Estado',max_length=9,choices=OpEstTraslado)
    descripcionTraslado = models.TextField(verbose_name='Descripcion', max_length=200)
    guardado = models.BooleanField(verbose_name='Guardado',default=False)

    def __unicode__(self):
        return self.codigoTraslado

    class Meta:
        ordering = ['-fechaTraslado']

class DetalleTraslado (models.Model):
    traslado = models.ForeignKey(Traslado)
    pesoTraslado = models.DecimalField(max_digits=9, decimal_places=3,verbose_name='Peso Traslado (grs)',default=0,null=True)
    unidadesTraslado = models.IntegerField(verbose_name='Unidades', default=0,null=True)
    productoTraslado = models.ForeignKey(Producto,null=True,blank=True)
    SubProducto = models.ForeignKey(SubProducto,null=True,blank=True)
    pesoEnvio = models.DecimalField(max_digits=9, decimal_places=3,verbose_name='Peso Envio (grs)',default=0)
    pesoLlegada = models.DecimalField(max_digits=9, decimal_places=3,verbose_name='Peso Llegada (grs)', null=True, default=0)

class Proveedor (models.Model):
    codigoProveedor = models.AutoField(primary_key=True)
    nit = models.CharField(verbose_name='Nit', max_length=11)
    nombreProv= models.CharField(max_length=50,verbose_name='Nombre')
    direccionProv = models.CharField(max_length=50, verbose_name='Direccion')
    telefonoProv = models.CharField(max_length=10,verbose_name='Telefono')
    email = models.EmailField(verbose_name='E-Mail')
    contacto = models.CharField(verbose_name='Contacto', max_length=50)
    ciudad = models.CharField(verbose_name='Ciudad',max_length=50)
    departamento = models.CharField (max_length=50)

    def __unicode__(self):

        return self.nombreProv

class Compra(models.Model):

    codigoCompra = models.AutoField(primary_key=True)
    fechaCompra = models.DateField(verbose_name='Fecha',blank=True,null=True)
    tipo = models.ForeignKey(Grupo)
    bodegaCompra = models.ForeignKey(Bodega,blank=True,default=5,verbose_name='Punto')
    #encargado = models.ForeignKey(Empleado)
    proveedor = models.ForeignKey(Proveedor)
    cantCabezas = models.IntegerField(verbose_name='# Cabezas', default=0)
    vrCompra = models.IntegerField(verbose_name='Valor Compra', default=0)
    vrTransporte = models.IntegerField(verbose_name='Transporte',default= 0)
    guardado = models.BooleanField(default=False)

    def __unicode__(self):
        cadena = "%s -- $%d"%(str(self.fechaCompra),self.vrCompra)
        return cadena

class Ganado(models.Model):

    tipoPiel = (
        (25000,'Calentana'),
        (44000,'Friana'),
    )

    codigoGanado = models.AutoField(primary_key=True, verbose_name='Codigo Ganado')
    compra = models.ForeignKey(Compra,blank=True,null=True)
    #piel = models.IntegerField(verbose_name='Piel', choices= tipoPiel,blank=True,default=0)
    pesoEnPie = models.DecimalField(verbose_name = 'Peso en Pie (grs)',max_digits=9, decimal_places=3)
    precioKiloEnPie = models.IntegerField(verbose_name='Precio Kilo en Pie')
    precioTotal = models.IntegerField(verbose_name='Precio Total')
    fechaIngreso = models.DateField(auto_now=True, blank=True, null=True)
    TotalpesoEnPie = models.DecimalField(verbose_name = 'Peso en Pie (grs)',max_digits=9, decimal_places=3,default=0)

    def __unicode__(self):
        return self.codigoGanado

class DetalleCompra(models.Model):
    compra = models.ForeignKey(Compra)
    producto = models.ForeignKey(Producto, null=True, blank=True)
    ganado = models.ForeignKey(Ganado, null=True, blank=True)
    pesoProducto = models.DecimalField(verbose_name = 'Peso(grs)',max_digits=15   , decimal_places=3,null= True,default=0)
    unidades = models.IntegerField(verbose_name='Unidades', null= True,default=0)
    subtotal = models.BigIntegerField(verbose_name='Vr.Factura',default=0)
    vrCompraProducto = models.BigIntegerField(verbose_name = 'Costo Kilo/Unidad',default= 0)
    pesoDescongelado = models.DecimalField(verbose_name = 'Peso Desc(grs)',max_digits=15   , decimal_places=3,null= True,default=0)
    vrKiloDescongelado = models.BigIntegerField(verbose_name = 'Costo Kilo/Desc.',default= 0)
    estado = models.BooleanField()

    def __unicode__(self):
        return self.id


class PlanillaRecepcion(models.Model):

    TipoGanado = (
        ('Mayor','Mayor'),
        ('Menor' , 'Menor'),
    )

    trans = (
        ('Frigovito','Frigovito'),
        ('Particular' , 'Particular'),
    )
    codigoRecepcion = models.AutoField(primary_key=True)
    compra = models.ForeignKey(Compra)
    #empleado = models.ForeignKey(Empleado)
    tipoGanado = models.CharField(verbose_name='Tipo Ganado', choices=TipoGanado, max_length=11)
    fechaRecepcion = models.DateField(verbose_name='Fecha')
    cantCabezas = models.IntegerField(verbose_name='# Cabezas', default=0)
    provedor = models.ForeignKey(Proveedor)
    vrTransporte = models.IntegerField(verbose_name='Vr.Transporte',default=0)
    transporte = models.CharField(verbose_name='Transporte', choices=trans, max_length=11)
    difPieCanal = models.DecimalField(verbose_name='Diferencia de pie A canal',default=0,max_digits=9, decimal_places=3)
    pesoCanales = models.DecimalField(verbose_name='Peso Canales',default=0,max_digits=9, decimal_places=3)
    vrKiloCanal = models.IntegerField(verbose_name='Vr. Kilo Canal',default=0)


    def __unicode__(self):
        return self.codigoRecepcion


class Movimientos(models.Model):
    tipo = models.CharField(verbose_name='Tipo',max_length=20)
    productoMov = models.ForeignKey(Producto)
    nombreProd = models.CharField(max_length=50,verbose_name='Nombre Producto',blank=True)
    fechaMov = models.DateField(verbose_name='Fecha')
    desde = models.CharField(max_length=30,blank=True)
    Hasta = models.CharField(max_length=30,blank=True)
    entrada = models.DecimalField(verbose_name='Entrada',default=0,max_digits=9, decimal_places=3)
    salida = models.DecimalField(verbose_name='Salida',default=0,max_digits=9, decimal_places=3)

class Ajustes(models.Model):
    fechaAjuste = models.DateField(verbose_name='Fecha',auto_now=True)
    productoAjuste = models.ForeignKey(Producto,verbose_name='Producto')
    bodegaAjuste = models.ForeignKey(Bodega,verbose_name='Bodega')
    cantidadActual = models.DecimalField(verbose_name='Cantidad actual',default=0,max_digits=9, decimal_places=3)
    unidadActual = models.DecimalField(verbose_name='Unidad actual',default=0,max_digits=9, decimal_places=3)
    pesoAjuste = models.DecimalField(verbose_name='Ajuste',default=0,max_digits=9, decimal_places=3)
    unidades = models.IntegerField(verbose_name='Unidades', null= True,default=0)
    observacion = models.TextField(verbose_name='Observaciones',max_length=150)
    sumar = models.BooleanField(default=False)
    restar = models.BooleanField(default=False)
    guardado = models.BooleanField(default=False)

class Faltantes(models.Model):
    fechaFaltante = models.DateField(verbose_name='Fecha')
    bodegaFaltante = models.ForeignKey(Bodega,verbose_name='Bodega')
    guardado = models.BooleanField(default=False)

    def __unicode__(self):
        return self.id

class DetalleFaltantes(models.Model):
    faltante = models.ForeignKey(Faltantes,verbose_name='Faltante')
    productoFaltante = models.ForeignKey(Producto,verbose_name='Producto')
    pesoActual = models.DecimalField(verbose_name='Peso Actual',default=0,max_digits=9, decimal_places=3)
    unidadActual = models.IntegerField(verbose_name='Unidad Actual', null= True,default=0)
    pesoFisico = models.DecimalField(verbose_name='Peso Fisico',default=0,max_digits=9, decimal_places=3)
    unidadFisica = models.IntegerField(verbose_name='Unidad Fisica', null= True,default=0)
    diferencia = models.DecimalField(verbose_name='Diferencia',default=0,max_digits=9, decimal_places=3)