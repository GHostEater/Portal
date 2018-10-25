# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from dept.models import Dept


class Application(models.Model):
    sex_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    student_status_choices = (
        ('Undergraduate', 'Undergraduate'),
        ('Graduate', 'Graduate'),
    )
    request_type_choices = (
        ('Fresh Request', 'Fresh Request'),
        ('Reprint', 'Reprint'),
    )
    region_choices = (
        ('Local', 'Local'),
        ('Foreign', 'Foreign'),
    )
    region_detail_choices = (
        ('Africa', 'Africa'),
        ('North America', 'North America'),
        ('South America', 'South America'),
        ('Europe', 'Europe'),
        ('Asia', 'Asia'),
        ('Oceania', 'Oceania'),
    )

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    matric_no = models.CharField(max_length=50)
    email = models.EmailField(max_length=255, null=True, blank=True)
    date_birth = models.DateField()
    phone = models.CharField(max_length=255)
    nationality = models.TextField()
    sex = models.CharField(max_length=255, choices=sex_choices)
    dept = models.ForeignKey(Dept)
    mode_of_entry = models.CharField(max_length=255)
    year_admission = models.CharField(max_length=255)
    year_graduation = models.CharField(max_length=255, null=True, blank=True)
    student_status = models.CharField(max_length=255, choices=student_status_choices)
    degree = models.CharField(max_length=255, null=True, blank=True)
    degree_date = models.DateField(null=True, blank=True)
    purpose = models.TextField()
    address_to = models.TextField()
    region = models.TextField(choices=region_choices, default='Local')
    region_detail = models.TextField(choices=region_detail_choices, null=True, blank=True)
    request_type = models.CharField(max_length=255, choices=request_type_choices)
    status = models.IntegerField(default=0)
    date_applied = models.DateTimeField()
