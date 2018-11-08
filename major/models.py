# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from dept.models import Dept

# Create your models here.


class Major(models.Model):
    name = models.CharField(max_length=255, default='')
    tcg = models.IntegerField(default='')
    dept = models.ForeignKey(Dept)
    degree = models.CharField(max_length=255, default='')

    def __str__(self):
        return str(self.name)
