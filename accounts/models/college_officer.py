# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from accounts.models import User
from college.models import College


class CollegeOfficer(models.Model):
    user = models.OneToOneField(User)
    college = models.OneToOneField(College, null=True, blank=True)

    def __str__(self):
        return str(self.user.last_name) + ", " + str(self.user.first_name) + " " + str(self.user.username)
