# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *

from django.contrib import admin

# Register your models here.



class HackDataAdmin(admin.ModelAdmin):
    list_display = (
        'problem_statement','identifier','attribute1','attribute2', 'attribute3','attribute4','attribute5','target')


admin.site.register(HackData, HackDataAdmin)