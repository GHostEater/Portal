# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class SysInfo(models.Model):
    name = models.CharField(max_length=256)
    short_name = models.CharField(max_length=256)
    med_name = models.CharField(max_length=256)
    long_name = models.CharField(max_length=256)
    slogan = models.CharField(max_length=256)
    receipt_name = models.CharField(max_length=256)
    site = models.CharField(max_length=256)
    result_email = models.CharField(max_length=256)
    noreply_email = models.CharField(max_length=256)
