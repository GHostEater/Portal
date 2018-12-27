# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from grade.models import Grade, GradePoint


class GradeAdmin(admin.ModelAdmin):
    list_display = ('grade', 'lower_limit', 'upper_limit', 'gp', 'active')


class GradePointAdmin(admin.ModelAdmin):
    list_display = ('grade', 'lower_limit', 'upper_limit', 'active')


admin.site.register(Grade, GradeAdmin)
admin.site.register(GradePoint, GradePointAdmin)
