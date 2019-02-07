# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from accounts.admin import admin_site
from transfer.models import IntraUni


class IntraUniAdmin(admin.ModelAdmin):
    list_display = ("student", 'major', 'reason', 'status', 'date', 'session', 'paid', 'handled_by')


admin_site.register(IntraUni, IntraUniAdmin)
