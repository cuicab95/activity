# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.contrib import admin

# Register your models here.


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'created_at_datetime')
    search_fields = ('id', 'title',)
    list_filter = ('status', )


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'property', 'schedule', 'status', 'created_at_datetime')
    search_fields = ('id', 'title',)
    list_filter = ('status',)
