# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from transfer.models import IntraUni


class IntraUniAdmin(admin.ModelAdmin):
    list_display = ("student", 'major', 'reason', 'status', 'date', 'session', 'paid', 'handled_by')


admin.site.register(IntraUni, IntraUniAdmin)
