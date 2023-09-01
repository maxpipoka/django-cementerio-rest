# Generated by Django 4.2.4 on 2023-09-01 04:31

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre Ciudad')),
            ],
            options={
                'verbose_name': 'Ciudad',
                'verbose_name_plural': 'Ciudades',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Deceased',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_death', models.DateField(verbose_name='Fecha de Fallecimiento')),
                ('is_child', models.CharField(choices=[('N', 'No'), ('S', 'Si')], default='N', max_length=1, verbose_name='Menor')),
            ],
            options={
                'verbose_name': 'Fallecido',
                'verbose_name_plural': 'Fallecidos',
            },
        ),
        migrations.CreateModel(
            name='Grave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parcel', jsonfield.fields.JSONField()),
                ('deceased', jsonfield.fields.JSONField(verbose_name='Fallecido/s')),
            ],
            options={
                'verbose_name': 'Sepultura',
                'verbose_name_plural': 'Sepulturas',
            },
        ),
        migrations.CreateModel(
            name='Parcel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Número')),
                ('row', models.CharField(max_length=2, verbose_name='Fila')),
            ],
            options={
                'verbose_name': 'Parcela',
                'verbose_name_plural': 'Parcelas',
            },
        ),
        migrations.CreateModel(
            name='Periodicity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('UNANIO', '1 AÑO'), ('CINCOANIOS', '5 AÑOS'), ('DIEZANIOS', '10 AÑOS')], max_length=10, verbose_name='Nombre')),
                ('years_amount', models.IntegerField(verbose_name='Años')),
            ],
            options={
                'verbose_name': 'Periodicidad',
                'verbose_name_plural': 'Periodicidades',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12, verbose_name='Nombre')),
                ('zone', models.CharField(choices=[('PRIMERA', '1RA'), ('SEGUNDA', '2DA'), ('NMUNICIPALES', 'NICHO MUNICIPAL')], max_length=12, verbose_name='Zona')),
            ],
            options={
                'verbose_name': 'Sector',
                'verbose_name_plural': 'Sectores',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre Provincia')),
                ('country', models.CharField(choices=[('ARGENTINA', 'ARGENTINA'), ('BRASIL', 'BRASIL'), ('PARAGUAY', 'PARAGUAY')], default='ARGENTINA', max_length=50, verbose_name='País')),
            ],
            options={
                'verbose_name': 'Provincia',
                'verbose_name_plural': 'Provincias',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Tax',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('zone', models.CharField(choices=[('PRIMERA', '1RA'), ('SEGUNDA', '2DA'), ('NMUNICIPALES', 'NICHO MUNICIPAL')], max_length=20, verbose_name='Zona')),
                ('periodicity', models.IntegerField(choices=[(1, '1 AÑO'), (5, '5 AÑOS'), (10, '10 AÑOS')], default=1, verbose_name='Periodo')),
                ('amount', models.FloatField(verbose_name='Monto')),
                ('date_from', models.DateField(verbose_name='Fecha Desde')),
                ('date_until', models.DateField(blank=True, null=True, verbose_name='Fecha Hasta')),
            ],
            options={
                'verbose_name': 'Tasa',
                'verbose_name_plural': 'Tasas',
            },
        ),
        migrations.CreateModel(
            name='Taxpayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(verbose_name='Código')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('dni', models.IntegerField(verbose_name='DNI')),
                ('adress', models.CharField(max_length=150, verbose_name='Dirección')),
                ('city_adress', models.CharField(max_length=50, verbose_name='Localidad')),
            ],
            options={
                'verbose_name': 'Contribuyente',
                'verbose_name_plural': 'Contribuyentes',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='RegistrationOffice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_office', models.CharField(max_length=100, verbose_name='Oficina del Registro')),
                ('registration_city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='register.city', verbose_name='Ciudad')),
            ],
            options={
                'verbose_name': 'Of.Registro',
                'verbose_name_plural': 'Ofs.Registro',
                'ordering': ['registration_office'],
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_number', models.IntegerField(verbose_name='Número Recibo')),
                ('payment_date', models.DateField(verbose_name='Fecha de Pago')),
                ('surcharge', models.FloatField(verbose_name='Recargos')),
                ('observations1', models.CharField(max_length=200, verbose_name='Obs 1')),
                ('observations2', models.CharField(max_length=100, verbose_name='Obs 2')),
                ('deceased', models.ManyToManyField(to='register.deceased')),
                ('parcel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='register.parcel')),
                ('tax', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='register.tax')),
                ('taxpayer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='register.taxpayer')),
            ],
            options={
                'verbose_name': 'Pago',
                'verbose_name_plural': 'Pagos',
            },
        ),
        migrations.AddField(
            model_name='parcel',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='register.sector'),
        ),
        migrations.AddField(
            model_name='deceased',
            name='deceased',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='register.taxpayer', verbose_name='Fallecido'),
        ),
        migrations.CreateModel(
            name='County',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre Departamento/Partido')),
                ('state', models.ForeignKey(default='1', on_delete=django.db.models.deletion.PROTECT, to='register.state')),
            ],
            options={
                'verbose_name': 'Departamento/Partido',
                'verbose_name_plural': 'Departamentos/Partidos',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='city',
            name='county',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.PROTECT, to='register.county'),
        ),
        migrations.CreateModel(
            name='BurialPermit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_in_registration_office', models.DateField(verbose_name='Fecha en Of. Registro')),
                ('presentation_date', models.DateField(verbose_name='Fecha de Presentación')),
                ('observations', models.TextField(blank=True, null=True, verbose_name='Observaciones')),
                ('documents', models.FileField(blank=True, null=True, upload_to='burialpermits/', verbose_name='Documentos')),
                ('deceased', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='register.deceased', verbose_name='Fallecido:')),
                ('presented_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='register.taxpayer', verbose_name='Presentado por:')),
                ('registration_office', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='register.registrationoffice')),
            ],
            options={
                'verbose_name': 'Perm.Inhum',
                'verbose_name_plural': 'Perms.Inhum',
                'ordering': ['presentation_date'],
            },
        ),
    ]