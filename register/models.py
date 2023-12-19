from django.db import models
from jsonfield.fields import JSONField

# Create your models here.

class Taxpayer(models.Model):
    code = models.IntegerField('Código', blank=False,)
    name = models.CharField('Nombre', max_length=100, blank=False, null=False)
    dni = models.IntegerField('DNI', blank=False, null=False)
    address = models.CharField(
        'Dirección', max_length=150, blank=False, null=False)
    city_address = models.CharField(
        'Localidad', max_length=50, blank=False, null=False)

    class Meta:
        verbose_name = 'Contribuyente'
        verbose_name_plural = 'Contribuyentes'
        ordering = ['name']

    def __str__(self):
        return self.name
    

class Deceased(models.Model):

    TRUEFALSE = [
        ('N', 'No'),
        ('S', 'Si'),
    ]
    deceased = models.ForeignKey(
        Taxpayer, verbose_name='Fallecido', on_delete=models.PROTECT)
    date_of_death = models.DateField(
        'Fecha de Fallecimiento', auto_now_add=False, blank=False, null=False)
    is_child = models.CharField('Menor', max_length=1, blank=False,
                                null=False, choices=TRUEFALSE, default='N')

    class Meta:
        verbose_name = 'Fallecido'
        verbose_name_plural = 'Fallecidos'
        # ordering = ['deceased']

    def __str__(self):
        return str(self.deceased.dni) + " - " + self.deceased.name
    

class State(models.Model):

    COUNTRIES = [
        ('ARGENTINA', 'ARGENTINA'),
        ('BRASIL', 'BRASIL'),
        ('PARAGUAY', 'PARAGUAY'),
    ]

    name = models.CharField(
        'Nombre Provincia', blank=False, max_length=50, null=False)
    country = models.CharField(
        'País', blank=False, max_length=50, choices=COUNTRIES, default='ARGENTINA')

    class Meta:
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'
        ordering = ['name']
    
    def __str__(self):
        return self.name + ' - ' + self.country




class County(models.Model):

    name = models.CharField(
        'Nombre Departamento/Partido', blank=False, max_length=50, null=False)
    state = models.ForeignKey(
        State, on_delete=models.PROTECT, default='1')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Departamento/Partido'
        verbose_name_plural = 'Departamentos/Partidos'
        ordering = ['name']



class City(models.Model):

    name = models.CharField(
        'Nombre Ciudad', blank=False, max_length=50, null=False)
    county = models.ForeignKey(County, on_delete=models.PROTECT, default='1')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
        ordering = ['name']



class RegistrationOffice(models.Model):
    registration_office = models.CharField(
        'Oficina del Registro', max_length=100, blank=False, null=False)
    registration_city = models.ForeignKey(
        City, on_delete=models.PROTECT, verbose_name='Ciudad')

    class Meta:
        verbose_name = 'Of.Registro'
        verbose_name_plural = 'Ofs.Registro'
        ordering = ['registration_office']

    def __str__(self):
        return self.registration_office + " - " + self.registration_city.name


class BurialPermit(models.Model):
    date_in_registration_office = models.DateField(
        'Fecha en Of. Registro', auto_now_add=False, blank=False, null=False)
    presentation_date = models.DateField(
        'Fecha de Presentación', auto_now_add=False, blank=False, null=False)
    deceased = models.ForeignKey(
        Deceased, on_delete=models.PROTECT, verbose_name='Fallecido:')
    presented_by = models.ForeignKey(
        Taxpayer, on_delete=models.PROTECT, verbose_name='Presentado por:')
    registration_office = models.ForeignKey(
        RegistrationOffice, on_delete=models.PROTECT)
    observations = models.TextField('Observaciones', blank=True, null=True)
    documents = models.FileField(
        verbose_name='Documentos', upload_to='burialpermits/', blank=True, null=True)

    class Meta:
        verbose_name = 'Perm.Inhum'
        verbose_name_plural = 'Perms.Inhum'
        ordering = ['presentation_date']

    def __str__(self):
        return str(self.presentation_date) + " - " + str(self.deceased.deceased.name) + " - " + str(self.deceased.deceased.dni)


class Sector(models.Model):

    ZONES = [
        ('PRIMERA', '1RA'),
        ('SEGUNDA', '2DA'),
        ('NMUNICIPALES', 'NICHO MUNICIPAL'),
    ]

    name = models.CharField(
        'Nombre', blank=False, max_length=12, null=False)
    zone = models.CharField(
        'Zona', blank=False, max_length=12, null=False, choices=ZONES)

    def __str__(self):
        return self.name + ' - ' + self.zone

    class Meta:
        verbose_name = 'Sector'
        verbose_name_plural = 'Sectores'
        ordering = ['name']


class Periodicity(models.Model):

    PERIODICIDAD = [
        ('UNANIO', '1 AÑO'),
        ('CINCOANIOS', '5 AÑOS'),
        ('DIEZANIOS', '10 AÑOS'),
    ]

    def set_years_amount(self):

        ANIOS_PERIODICIDAD = [
            ('UNANIO', '1'),
            ('CINCOANIOS', '5'),
            ('DIEZANIOS', '10'),
        ]
        return ANIOS_PERIODICIDAD[self.name]

    def save(self, *args, **kargs):
        if not self.years_amount:
            self.years_amount = self.set_years_amount()
        super(Periodicity, self).save(*args, **kargs)

    name = models.CharField('Nombre', max_length=10, blank=False,
                            null=False, choices=PERIODICIDAD)
    years_amount = models.IntegerField('Años', blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Periodicidad'
        verbose_name_plural = 'Periodicidades'
        ordering = ['name']


class Parcel(models.Model):
    number = models.IntegerField('Número', blank=False, null=False, )
    row = models.CharField('Fila', max_length=2, blank=False, null=False)
    sector = models.ForeignKey(Sector, on_delete=models.PROTECT)
    # zone = models.ForeignKey(Zone, on_delete=models.PROTECT)

    def __str__(self):
        # return "Zona " + (self.zone.name + ' - Sector: ' + self.sector + '- Fila: ' + str(self.row) + ' - N: ' + str(self.number))
        return "Zona: " + str(self.sector.zone) + ' - Sector: ' + str(self.sector.name) + ' - Fila: ' + str(self.row) + ' - N°: ' + str(self.number)

    class Meta:
        verbose_name = 'Parcela'
        verbose_name_plural = 'Parcelas'


class Grave(models.Model):
    parcel = JSONField()
    deceased = JSONField(verbose_name='Fallecido/s')

    class Meta:
        verbose_name = 'Sepultura'
        verbose_name_plural = 'Sepulturas'


class Tax(models.Model):

    ZONES = [
        ('PRIMERA', '1RA'),
        ('SEGUNDA', '2DA'),
        ('NMUNICIPALES', 'NICHO MUNICIPAL'),
    ]

    PERIODICITY = [
        (1, '1 AÑO'),
        (5, '5 AÑOS'),
        (10, '10 AÑOS'),
    ]

    name = models.CharField('Nombre', max_length=100, blank=False, null=False)
    zone = models.CharField('Zona', blank=False,
                            null=False, max_length=20, choices=ZONES)
    periodicity = models.IntegerField(
        'Periodo', blank=False, null=False, choices=PERIODICITY, default=1)
    amount = models.FloatField('Monto', blank=False, null=False)
    date_from = models.DateField(
        'Fecha Desde', auto_now_add=False, blank=False, null=False)
    date_until = models.DateField(
        'Fecha Hasta', auto_now_add=False, blank=True, null=True)

    def __str__(self):
        return self.name + " - $" + str(self.amount)

    class Meta:
        verbose_name = 'Tasa'
        verbose_name_plural = 'Tasas'


class Payment(models.Model):
    receipt_number = models.IntegerField(
        'Número Recibo', blank=False, null=False)
    payment_date = models.DateField(
        'Fecha de Pago', auto_now_add=False, blank=False, null=False)
    deceased = models.ManyToManyField(Deceased)
    taxpayer = models.ForeignKey(Taxpayer, on_delete=models.PROTECT)
    parcel = models.ForeignKey(Parcel, on_delete=models.PROTECT)
    tax = models.ForeignKey(Tax, on_delete=models.PROTECT)
    surcharge = models.FloatField('Recargos', blank=False, null=False)
    observations1 = models.CharField(
        'Obs 1', max_length=200, blank=False, null=False)
    observations2 = models.CharField(
        'Obs 2', max_length=100, blank=False, null=False)

    def __str__(self):
        return str(self.payment_date) + " - " + str(self.receipt_number) + " - " + self.taxpayer.name + " - $" + str(self.tax.amount) + " - $" + str(self.surcharge)

    class Meta:
        verbose_name = "Pago"
        verbose_name_plural = "Pagos"
