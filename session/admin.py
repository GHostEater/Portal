# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from accounts.admin import admin_site
from session.models import Session

# Register your models here.


class SessionAdmin(admin.ModelAdmin):
    list_display = ("session", "is_current", "is_admission", "actions")
    
admin_site.register(Session, SessionAdmin)
