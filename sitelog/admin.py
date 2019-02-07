# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from accounts.admin import admin_site
from sitelog.models import Log

# Register your models here.


class LogAdmin(admin.ModelAdmin):
    list_display = ('action', 'user', 'role', 'date', 'location')
    search_fields = ('action', 'user', 'role')


admin_site.register(Log, LogAdmin)
