# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models.signals import post_save

from accounts.models import StudentAffairs, CollegeOfficer, Lecturer, Dean, User
from accounts.models import AcademicAffairs
from accounts.models import Bursar


def create_profile(sender, **kwargs):
    if kwargs['created']:
        if kwargs['instance'].type == '2':
            acad = AcademicAffairs.objects.create(user=kwargs['instance'])
        if kwargs['instance'].type == '3':
            acad = Bursar.objects.create(user=kwargs['instance'])
        if kwargs['instance'].type == '4':
            acad = StudentAffairs.objects.create(user=kwargs['instance'])
        if kwargs['instance'].type == '5':
            acad = CollegeOfficer.objects.create(user=kwargs['instance'])
        if kwargs['instance'].type == '6':
            acad = Lecturer.objects.create(user=kwargs['instance'])
        if kwargs['instance'].type == '8':
            acad = Dean.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
