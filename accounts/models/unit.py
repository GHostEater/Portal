# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Unit(models.Model):
    name = models.CharField(max_length=255)
    rank = models.IntegerField()

    def __str__(self):
        return str(self.name)
