# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from session.models import Session

# Register your models here.


class SessionAdmin(admin.ModelAdmin):
    list_display = ("session", "is_current", "is_admission", "actions")
    
admin.site.register(Session, SessionAdmin)
