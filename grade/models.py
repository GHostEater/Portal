# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from dept.models import Dept


class Grade(models.Model):
    grade = models.CharField(max_length=5)
    lower_limit = models.FloatField()
    upper_limit = models.FloatField()
    dept = models.ForeignKey(Dept)
