# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from grade.models import Grade


class GradeAdmin(admin.ModelAdmin):
    list_display = ('grade', 'lower_limit', 'upper_limit', 'gp')


admin.site.register(Grade, GradeAdmin)
