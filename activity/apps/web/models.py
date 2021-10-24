# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.contrib.postgres.fields import JSONField
from django.db import models

# Create your models here.


class RowControl(models.Model):
    STATUS_CHOICES = (
        ('ACT', 'Activado'),
        ('DES', 'Desactivado'),
    )
    created_at_datetime = models.DateTimeField(auto_now_add=True, verbose_name=_("Fecha de creación"))
    updated_at_datetime = models.DateTimeField(auto_now_add=True, verbose_name=_("Fecha de actualización"))
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='ACT')

    class Meta:
        abstract = True
        verbose_name = _("Control de cambios")
        verbose_name_plural = _("Control de cambios")


class Property(RowControl):
    title = models.CharField(max_length=255, verbose_name=_("Título"))
    address = models.TextField(verbose_name=_("Dirección"))
    description = models.TextField(verbose_name=_("Descripción"))
    disabled_at_datetime = models.DateTimeField(verbose_name=_("Fecha de deshabilitación"), null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Propiedad")
        verbose_name_plural = _("Propiedades")


class Activity(RowControl):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, verbose_name=_("Propiedad"))
    schedule = models.DateTimeField(verbose_name=_("Fecha agendada"))
    title = models.CharField(max_length=255, verbose_name=_("Título"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Actividad")
        verbose_name_plural = _("Actividades")


class Survey(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, verbose_name=_("Actividad"))
    answers = JSONField(verbose_name=_("Respuestas"))
    created_at_datetime = models.DateTimeField(auto_now_add=True, verbose_name=_("Fecha de creación"))

    def __str__(self):
        return self.activity.title

    class Meta:
        verbose_name = _("Encuesta")
        verbose_name_plural = _("Encuestas")