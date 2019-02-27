# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from major.models import Major
from session.models import Session
from level.models import Level

# Create your models here.


class Application(models.Model):
    cert_choices = (
        ('WAEC', 'WAEC'),
        ('NECO', 'NECO'),
        ('NABTEB', 'NABTEB'),
        ('A\'Levels', 'A\'Levels'),
    )
    degree_choices = (
        ('IJMB', 'IJMB'),
        ('JUPEB', 'JUPEB'),
        ('NCE', 'NCE'),
        ('ND', 'ND'),
        ('HND', 'HND'),
    )
    comp_lit_choices = (
        ('Good', 'Good'),
        ('Fair', 'Fair'),
        ('No', 'No'),
    )
    offence_choices = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    programme_type_choices = (
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Executive', 'Executive'),
    )
    programme_choices = (
        ('Undergraduate', 'Undergraduate'),
        ('Undergraduate Transfer', 'Undergraduate Transfer'),
        ('Postgraduate', 'Postgraduate'),
        ('JUPEB', 'JUPEB'),
    )
    mode_of_entry_choices = (
        ('UTME Candidate', 'UTME Candidate'),
        ('Transfer', 'Transfer'),
        ('Direct Entry', 'Direct Entry'),
        ('Conversion', 'Conversion'),
    )
    residence_choices = (
        ('Residential', 'Residential'),
        ('Off Campus', 'Off Campus'),
    )

    app_no = models.CharField(max_length=256, null=True, blank=True)
    programme = models.CharField(max_length=200, choices=programme_choices)
    programme_type = models.CharField(max_length=200, choices=programme_type_choices, null=True, blank=True)
    mode_of_entry = models.CharField(max_length=200, choices=mode_of_entry_choices, null=True, blank=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_birth = models.DateField()
    sex = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)
    state_of_origin = models.CharField(max_length=200)
    lga = models.CharField(max_length=200)
    email = models.EmailField(unique=True, max_length=255)
    address = models.TextField()
    phone = models.CharField(max_length=200)
    religion = models.CharField(max_length=200)
    sponsor = models.TextField()
    sponsor_address = models.TextField()
    sponsor_phone = models.CharField(max_length=200)
    maiden_name = models.TextField(null=True, blank=True)
    marital_status = models.CharField(max_length=200, null=True, blank=True)
    passport_number = models.CharField(max_length=200, null=True, blank=True)
    post_address = models.TextField(null=True, blank=True)
    next_kin = models.TextField(null=True, blank=True)
    next_kin_phone = models.CharField(max_length=200, null=True, blank=True)
    next_kin_address = models.TextField(null=True, blank=True)
    institution_attended = models.TextField(null=True, blank=True)
    honours = models.TextField(null=True, blank=True)
    transcript = models.TextField(null=True, blank=True)
    transcript_img = models.ImageField(null=True, blank=True)
    year_entry = models.CharField(max_length=200, null=True, blank=True)
    residence = models.CharField(max_length=200, choices=residence_choices, null=True, blank=True)
    nysc = models.TextField(null=True, blank=True)
    nysc_img = models.ImageField(null=True, blank=True)
    appointments = models.TextField(null=True, blank=True)
    publications = models.TextField(null=True, blank=True)
    current_course = models.TextField(null=True, blank=True)
    disability = models.CharField(max_length=50, null=True, blank=True)
    additional_info = models.TextField(null=True, blank=True)
    objection = models.CharField(max_length=200, choices=offence_choices, null=True, blank=True)
    duration = models.CharField(max_length=200, null=True, blank=True)
    cert1 = models.CharField(max_length=200, choices=cert_choices, null=True, blank=True)
    cert1_date = models.CharField(max_length=200, null=True, blank=True)
    cert1_subject = models.TextField(null=True, blank=True)
    cert1_img = models.ImageField(null=True, blank=True)
    cert2 = models.CharField(max_length=200, choices=cert_choices, null=True, blank=True)
    cert2_date = models.CharField(max_length=200, null=True, blank=True)
    cert2_subject = models.TextField(null=True, blank=True)
    cert2_img = models.ImageField(null=True, blank=True)
    degree = models.CharField(max_length=200, choices=degree_choices, null=True, blank=True)
    degree_class = models.CharField(max_length=200, null=True, blank=True)
    degree_img = models.ImageField(null=True, blank=True)
    jamb_no = models.CharField(max_length=200, null=True, blank=True, unique=True)
    jamb_score = models.CharField(max_length=200, null=True, blank=True)
    first_choice = models.TextField(null=True, blank=True)
    second_choice = models.TextField(null=True, blank=True)
    extracurricular = models.TextField(null=True, blank=True)
    comp_lit = models.CharField(max_length=200, choices=comp_lit_choices, null=True, blank=True)
    offence = models.CharField(max_length=200, choices=offence_choices, null=True, blank=True)
    offence_detail = models.TextField(null=True, blank=True)
    referee = models.TextField(null=True, blank=True)
    referee_address = models.TextField(null=True, blank=True)
    referee_phone = models.CharField(max_length=200, null=True, blank=True)
    session = models.ForeignKey(Session, null=True, blank=True)
    date_applied = models.DateTimeField()
    img = models.ImageField(null=True, blank=True)
    pin = models.CharField(max_length=200, null=True, blank=True)
    admitted = models.BooleanField(default=0)
    level = models.ForeignKey(Level, null=True, blank=True)
    choice = models.ForeignKey(Major, null=True, blank=True)
    reason_transfer = models.TextField(null=True, blank=True)
    curr_cgpa = models.TextField(null=True, blank=True)
    curr_uni = models.CharField(max_length=256, null=True, blank=True)
    curr_course = models.CharField(max_length=256, null=True, blank=True)
    curr_year_of_entry = models.CharField(max_length=256, null=True, blank=True)
    email_hod = models.EmailField(max_length=255, null=True, blank=True)
    email_dean = models.EmailField(max_length=255, null=True, blank=True)
    dean_comment = models.TextField(null=True, blank=True)
    hod_comment = models.TextField(null=True, blank=True)
    hod_signature = models.ImageField(null=True, blank=True)
    dean_signature = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.last_name+", "+self.first_name+" "+self.email+" "+self.phone+" "+self.programme+" "+str(self.session))


class Pin(models.Model):
    pin = models.CharField(max_length=20, unique=True)
    used = models.BooleanField(default=0)
    date_used = models.DateTimeField(null=True, blank=True)
    application = models.ForeignKey(Application, null=True, blank=True, related_name='pin_application')
