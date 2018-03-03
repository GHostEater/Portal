# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from latereg.models import RegStatus, LateReg, Log

# Register your models here.
admin.site.register(RegStatus)
admin.site.register(LateReg)
admin.site.register(Log)
