# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.contrib.auth.hashers import make_password

from accounts.models import Unit


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
    nationality = models.CharField(max_length=256, null=True, blank=True)
    state_origin = models.CharField(max_length=256, null=True, blank=True)
    lga = models.CharField(max_length=256, null=True, blank=True)
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
    sign = models.ImageField(null=True, blank=True)
    mail_prefix = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return str(self.last_name+", "+self.first_name+" "+self.username+" User Type:"+self.type)


@receiver(pre_save, sender='accounts.User')
def my_callback(sender, instance, *args, **kwargs):
    new_password = instance.password
    try:
        old_password = User.objects.get(pk=instance.pk).password
    except User.DoesNotExist:
        old_password = None
    if new_password != old_password:
        instance.password = make_password(instance.password)


# def create_profile(sender, **kwargs):
#     if kwargs['created']:
#         if kwargs['instance'].type == '2':
#             AcademicAffairs.objects.create(user=kwargs['instance'])
#         if kwargs['instance'].type == '3':
#             Bursar.objects.create(user=kwargs['instance'])
#         if kwargs['instance'].type == '4':
#             StudentAffairs.objects.create(user=kwargs['instance'])
#         if kwargs['instance'].type == '5':
#             CollegeOfficer.objects.create(user=kwargs['instance'])
#         if kwargs['instance'].type == '6':
#             Lecturer.objects.create(user=kwargs['instance'])
#         if kwargs['instance'].type == '8':
#             Dean.objects.create(user=kwargs['instance'])
#
# post_save.connect(create_profile, sender=User)
