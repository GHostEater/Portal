# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from accounts.models import User
from level.models import Level
from major.models import Major
from modeofentry.models import ModeOfEntry


class Student(models.Model):
    olevel_choices = (
        ('WAEC', 'WAEC'),
        ('NECO', 'NECO'),
        ('WAEC/GCE', 'WAEC/GCE'),
        ('NECO/GCE', 'NECO/GCE'),
        ('WAEC/NECO', 'WAEC/NECO'),
        ('NABTEB', 'NABTEB'),
        ("NABTEB/WAEC", "NABTEB/WAEC"),
        ("NABTEB/NECO", "NABTEB/NECO"),
        ("NABTEB/GCE", "NABTEB/GCE"),
    )
    status_choices = (
        ('1', 'Normal'),
        ('2', 'Exchange'),
        ('3', 'Leave'),
        ('4', 'Sick'),
        ('5', 'Suspension'),
        ('6', 'Deferment'),
        ('7', 'Withdrawn'),
        ('8', 'Graduated'),
    )
    programme_type_choices = (
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Executive', 'Executive'),
    )
    user = models.OneToOneField(User)
    parent_no = models.CharField(max_length=15, null=True, blank=True)
    parent_email = models.EmailField(max_length=255, null=True, blank=True)
    olevel = models.CharField(max_length=15, choices=olevel_choices, null=True, blank=True)
    major = models.ForeignKey(Major)
    level = models.ForeignKey(Level)
    mode_of_entry = models.ForeignKey(ModeOfEntry)
    status = models.CharField(max_length=15, choices=status_choices, default='1', blank=True)
    edit = models.BooleanField(default=False)
    programme_type = models.CharField(max_length=15, choices=programme_type_choices, default="Full Time", blank=True)

    def __str__(self):
        return str(self.user.last_name) + ", " + str(self.user.first_name) + " " + str(self.user.username)
