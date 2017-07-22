# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from dept.models import Dept

# Create your models here.


class Major(models.Model):
    name = models.CharField(max_length=50, default='')
    tcg = models.IntegerField(default='')
    dept = models.ForeignKey(Dept)

    def __str__(self):
        return str(self.name)
