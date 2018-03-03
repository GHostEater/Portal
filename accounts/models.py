# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth.hashers import make_password
from django.contrib.auth.validators import UnicodeUsernameValidator

from college.models import College
from dept.models import Dept
from major.models import Major
from modeofentry.models import ModeOfEntry
from level.models import Level

# Create your models here.


class Unit(models.Model):
    name = models.CharField(max_length=255)
    rank = models.IntegerField()

    def __str__(self):
        return str(self.name)


class User(AbstractUser):
    type_choices = (
        ('1', 'Admin'),
        ('2', 'Academic Affairs'),
        ('3', 'Bursar'),
        ('4', 'Student Affairs'),
        ('5', 'College Officer'),
        ('6', 'Lecturer'),
        ('7', 'Student'),
        ('8', 'Dean'),
        ('9', 'Non-Academic Staff'),
        ('10', 'Voter'),
    )
    sex_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    genotype_choices = (
        ('AA', 'AA'),
        ('AS', 'AS'),
        ('SS', 'SS'),
        ('CS', 'CS'),
        ('AC', 'AC'),
    )
    blood_group_choices = (
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    )
    username_validator = UnicodeUsernameValidator
    type = models.CharField(max_length=2, choices=type_choices, default='')
    sex = models.CharField(max_length=10, choices=sex_choices, default='')
    date_birth = models.DateField(null=True, default='1970-01-01')
    nationality = models.CharField(max_length=20, null=True, blank=True)
    state_origin = models.CharField(max_length=20, null=True, blank=True)
    lga = models.CharField(max_length=20, null=True, blank=True)
    religion = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    next_kin = models.TextField(null=True, blank=True)
    next_kin_address = models.TextField(null=True, blank=True)
    town = models.TextField(null=True, blank=True)
    genotype = models.CharField(max_length=5, choices=genotype_choices, null=True, blank=True)
    blood_group = models.CharField(max_length=5, choices=blood_group_choices, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    cv = models.FileField(null=True, blank=True)
    unit = models.ForeignKey(Unit, null=True, blank=True)
    profile_rank = models.IntegerField(null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    img = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.last_name) + ", " + str(self.first_name) + " " + str(self.username) + " User Type:" + str(self.type)


@receiver(pre_save, sender='accounts.User')
def my_callback(sender, instance, *args, **kwargs):
    new_password = instance.password
    try:
        old_password = User.objects.get(pk=instance.pk).password
    except User.DoesNotExist:
        old_password = None
    if new_password != old_password:
        instance.password = make_password(instance.password)


class CollegeOfficer(models.Model):
    user = models.OneToOneField(User)
    college = models.OneToOneField(College, null=True, blank=True)

    def __str__(self):
        return str(self.user.last_name) + ", " + str(self.user.first_name) + " " + str(self.user.username)


class StudentAffairs(models.Model):
    rank_choices = (
        ('1', 'Head'),
        ('2', 'Officer'),
    )
    user = models.OneToOneField(User)
    rank = models.CharField(max_length=2, choices=rank_choices, default=2)

    def __str__(self):
        return str(self.user.last_name) + ", " + str(self.user.first_name) + " " + str(self.user.username)


class AcademicAffairs(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return str(self.user.last_name) + ", " + str(self.user.first_name) + " " + str(self.user.username)


class Bursar(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return str(self.user.last_name) + ", " + str(self.user.first_name) + " " + str(self.user.username)


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


class Student(models.Model):
    olevel_choices = (
        ('WAEC', 'WAEC'),
        ('NECO', 'NECO'),
        ('WAEC/GCE', 'WAEC/GCE'),
        ('NECO/GCE', 'NECO/GCE'),
        ('WAEC/NECO', 'WAEC/NECO'),
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
    user = models.OneToOneField(User)
    parent_no = models.CharField(max_length=15, null=True, blank=True)
    olevel = models.CharField(max_length=15, choices=olevel_choices, null=True, blank=True)
    major = models.ForeignKey(Major)
    level = models.ForeignKey(Level)
    mode_of_entry = models.ForeignKey(ModeOfEntry)
    status = models.CharField(max_length=15, choices=status_choices, default='1', blank=True)
    edit = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.last_name) + ", " + str(self.user.first_name) + " " + str(self.user.username)


class Dean(models.Model):
    user = models.OneToOneField(User)
    college = models.OneToOneField(College, null=True, blank=True)

    def __str__(self):
        return str(self.user.last_name) + ", " + str(self.user.first_name) + " " + str(self.user.username)


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
