# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from accounts.admin import admin_site
from courseresultuploadlog.models import Log

admin_site.register(Log)
