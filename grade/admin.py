# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from accounts.admin import admin_site
from grade.models import Grade, GradePoint


class GradeAdmin(admin.ModelAdmin):
    list_display = ('grade', 'lower_limit', 'upper_limit', 'gp', 'active')


class GradePointAdmin(admin.ModelAdmin):
    list_display = ('grade', 'lower_limit', 'upper_limit', 'active')


admin_site.register(Grade, GradeAdmin)
admin_site.register(GradePoint, GradePointAdmin)
