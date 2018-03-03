# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Hostel(models.Model):
    sex_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    name = models.CharField(max_length=256)
    sex = models.CharField(max_length=10, choices=sex_choices, default='')

    def __str__(self):
        return str(self.name+" "+self.sex)
