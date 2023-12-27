# Generated by Django 4.2.4 on 2023-12-19 22:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_rename_adress_taxpayer_address_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='burialpermit',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='burialpermit',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 19, 19, 31, 0, 924956)),
        ),
        migrations.AddField(
            model_name='burialpermit',
            name='updatedAt',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='city',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 19, 19, 31, 0, 924956)),
        ),
        migrations.AddField(
            model_name='city',
            name='updatedAt',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='county',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='county',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 19, 19, 31, 0, 924956)),
        ),
        migrations.AddField(
            model_name='county',
            name='updatedAt',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='deceased',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='deceased',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 19, 19, 31, 0, 909330)),
        ),
        migrations.AddField(
            model_name='deceased',
            name='updatedAt',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='grave',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='grave',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 19, 19, 31, 0, 924956)),
        ),
        migrations.AddField(
            model_name='grave',
            name='updatedAt',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='parcel',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='parcel',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 19, 19, 31, 0, 924956)),
        ),
        migrations.AddField(
            model_name='parcel',
            name='updatedAt',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 19, 19, 31, 0, 924956)),
        ),
        migrations.AddField(
            model_name='payment',
            name='updatedAt',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='periodicity',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='periodicity',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 19, 19, 31, 0, 924956)),
        ),
        migrations.AddField(
            model_name='periodicity',
            name='updatedAt',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='registrationoffice',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='registrationoffice',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 19, 19, 31, 0, 924956)),
        ),
        migrations.AddField(
            model_name='registrationoffice',
            name='updatedAt',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='sector',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='sector',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 19, 19, 31, 0, 924956)),
        ),
        migrations.AddField(
            model_name='sector',
            name='updatedAt',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='state',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='state',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 19, 19, 31, 0, 924956)),
        ),
        migrations.AddField(
            model_name='state',
            name='updatedAt',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='tax',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='tax',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 19, 19, 31, 0, 924956)),
        ),
        migrations.AddField(
            model_name='tax',
            name='updatedAt',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='taxpayer',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='taxpayer',
            name='createdAt',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 19, 19, 31, 0, 909330)),
        ),
        migrations.AddField(
            model_name='taxpayer',
            name='updatedAt',
            field=models.DateTimeField(null=True),
        ),
    ]