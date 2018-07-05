# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from accounts.models import User


class StudentAffairs(models.Model):
    rank_choices = (
        ('1', 'Head'),
        ('2', 'Officer'),
    )
    user = models.OneToOneField(User)
    rank = models.CharField(max_length=2, choices=rank_choices, default=2)

    def __str__(self):
        return str(self.user.last_name) + ", " + str(self.user.first_name) + " " + str(self.user.username)
