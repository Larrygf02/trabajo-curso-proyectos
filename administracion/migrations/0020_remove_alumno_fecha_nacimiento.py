# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-09 19:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0019_auto_20170709_1413'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alumno',
            name='fecha_nacimiento',
        ),
    ]