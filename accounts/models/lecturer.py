# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from accounts.models import User
from dept.models import Dept


class Lecturer(models.Model):
    rank_choices = (
        ('Professor', 'Professor'),
        ('Associate Professor', 'Associate Professor'),
        ('Senior Lecturer', 'Senior Lecturer'),
        ('Lecturer I', 'Lecturer I'),
        ('Lecturer II', 'Lecturer II'),
        ('Assistant Lecturer', 'Assistant Lecturer'),
        ('Graduate Assistant', 'Graduate Assistant'),
    )
    status_choices = (
        ('Permanent', 'Permanent'),
        ('Adjunct', 'Adjunct'),
        ('Contract', 'Contract'),
    )
    user = models.OneToOneField(User)
    rank = models.CharField(max_length=20, choices=rank_choices, null=True, blank=True)
    status = models.CharField(max_length=20, choices=status_choices, null=True, blank=True)
    dept = models.ForeignKey(Dept, null=True, blank=True)

    def __str__(self):
        return str(self.user.last_name) + ", " + str(self.user.first_name) + " " + str(self.user.username)
