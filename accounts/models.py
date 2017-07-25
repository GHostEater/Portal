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
from modeOfEntry.models import ModeOfEntry
from level.models import Level

# Create your models here.


class User(AbstractUser):
    type_choices = (
        ('1', 'Admin'),
        ('2', 'Academic Affairs'),
        ('3', 'Bursar'),
        ('4', 'Student Affairs'),
        ('5', 'College Officer'),
        ('6', 'Lecturer'),
        ('7', 'Student'),
    )
    sex_choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    username_validator = UnicodeUsernameValidator
    type = models.CharField(max_length=2, choices=type_choices, default='')
    sex = models.CharField(max_length=10, choices=sex_choices, default='')

    def __str__(self):
        return str(self.last_name) + ", " + str(self.first_name) + " " + str(self.username)


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
    )
    user = models.OneToOneField(User)
    address = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    rank = models.CharField(max_length=20, choices=rank_choices, null=True, blank=True)
    status = models.CharField(max_length=20, choices=status_choices, null=True, blank=True)
    dept = models.ForeignKey(Dept, null=True, blank=True)

    def __str__(self):
        return str(self.user.last_name) + ", " + str(self.user.first_name) + " " + str(self.user.username)


class Student(models.Model):
    genotype_choices = (
        ('AA', 'AA'),
        ('AS', 'AS'),
        ('SS', 'SS'),
        ('CS', 'CS'),
    )
    bloodGroup_choices = (
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    )
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
        ('6', 'Withdrawn'),
        ('7', 'Graduated'),
    )
    user = models.OneToOneField(User)
    phone = models.CharField(max_length=20, null=True, blank=True)
    dateBirth = models.DateField(null=True, default='1970-01-01')
    nationality = models.CharField(max_length=20, null=True, blank=True)
    stateOrigin = models.CharField(max_length=20, null=True, blank=True)
    lga = models.CharField(max_length=20, null=True, blank=True)
    religion = models.CharField(max_length=20, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    nextKin = models.TextField(null=True, blank=True)
    nextKinAddress = models.TextField(null=True, blank=True)
    town = models.TextField(null=True, blank=True)
    genotype = models.CharField(max_length=5, choices=genotype_choices, null=True, blank=True)
    bloodGroup = models.CharField(max_length=5, choices=bloodGroup_choices, null=True, blank=True)
    parentNo = models.CharField(max_length=15, null=True, blank=True)
    oLevel = models.CharField(max_length=15, choices=olevel_choices, null=True, blank=True)
    major = models.ForeignKey(Major)
    level = models.ForeignKey(Level)
    modeOfEntry = models.ForeignKey(ModeOfEntry)
    status = models.CharField(max_length=15, choices=status_choices, default='1', blank=True)
    img = models.FileField(null=True, blank=True)

    def __str__(self):
        return str(self.user.last_name) + ", " + str(self.user.first_name) + " " + str(self.user.username)


def create_profile(sender, **kwargs):
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

post_save.connect(create_profile, sender=User)
