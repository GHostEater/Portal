# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from accounts.admin import admin_site
from latereg.models import RegStatus, LateReg, Log

# Register your models here.
admin_site.register(RegStatus)
admin_site.register(LateReg)
admin_site.register(Log)
