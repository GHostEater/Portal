# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from hostel.models import Hostel

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=256)
    size = models.IntegerField()
    hostel = models.ForeignKey(Hostel)

    def __str__(self):
        return str(self.name+" "+str(self.size)+" "+str(self.hostel))
