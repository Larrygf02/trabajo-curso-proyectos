# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-09 19:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0023_auto_20170709_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, null=True),
        ),
    ]
