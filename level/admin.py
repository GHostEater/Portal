# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from accounts.admin import admin_site
from level.models import Level

# Register your models here.

admin_site.register(Level)
