# Generated by Django 3.0.3 on 2020-04-23 03:09

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('googleplaces', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='geom',
            field=django.contrib.gis.db.models.fields.PointField(default=None, srid=4326),
        ),
    ]
