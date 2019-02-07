# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from accounts.admin import admin_site
from modeofentry.models import ModeOfEntry

# Register your models here.

admin_site.register(ModeOfEntry)
