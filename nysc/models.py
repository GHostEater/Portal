# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Nysc(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    matric_no = models.CharField(max_length=200, unique=True)
    jamb_no = models.CharField(max_length=200)
    date_birth = models.DateField()
    state_origin = models.CharField(max_length=200)
    marital_status = models.CharField(max_length=200)
    sex = models.CharField(max_length=200)
    programme = models.CharField(max_length=200)
    programme_type = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    parent_no = models.CharField(max_length=200)
    email = models.EmailField(max_length=255)
    date = models.DateTimeField()
    img = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.last_name+", "+self.first_name+" "+self.middle_name+", Date Applied:"+str(self.date))
