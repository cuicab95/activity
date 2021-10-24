# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-10-24 20:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='schedule',
            field=models.DateTimeField(verbose_name='Fecha agendada'),
        ),
        migrations.AlterField(
            model_name='activity',
            name='status',
            field=models.CharField(choices=[('ACT', 'Activado'), ('DES', 'Desactivado'), ('REA', 'Realizada')], default='ACT', max_length=3),
        ),
        migrations.AlterField(
            model_name='property',
            name='status',
            field=models.CharField(choices=[('ACT', 'Activado'), ('DES', 'Desactivado'), ('REA', 'Realizada')], default='ACT', max_length=3),
        ),
    ]
