# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class College(models.Model):
    name = models.CharField(max_length=255, default='')
    acronym = models.CharField(max_length=50, default='')

    def __str__(self):
        return str(self.acronym)
