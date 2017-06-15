# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth.hashers import make_password

# Create your models here.


class Session(models.Model):
    session = models.CharField(max_length=20, default='')
    is_current = models.BooleanField(default='1')

    def __str__(self):
        return str(self.session)


class Semester(models.Model):
    semester = models.CharField(max_length=20, default='')

    def __str__(self):
        return str(self.semester)


class Level(models.Model):
    level = models.CharField(max_length=20, default='')

    def __str__(self):
        return str(self.level)


class ModeOfEntry(models.Model):
    name = models.CharField(max_length=20, default='')

    def __str__(self):
        return str(self.name)


class College(models.Model):
    name = models.CharField(max_length=50, default='')
    acronym = models.CharField(max_length=20, default='')

    def __str__(self):
        return str(self.acronym)


class Dept(models.Model):
    name = models.CharField(max_length=50, default='')
    college = models.ForeignKey(College, default=0)

    def __str__(self):
        return str(self.name)


class Major(models.Model):
    name = models.CharField(max_length=50, default='')
    tcg = models.IntegerField(default='')
    dept = models.ForeignKey(Dept, default=0)

    def __str__(self):
        return str(self.name)


class Course(models.Model):
    code = models.CharField(max_length=20)
    title = models.CharField(max_length=50)
    unit = models.CharField(max_length=10)
    type = models.CharField(max_length=2)
    semester = models.IntegerField(default=0)
    level = models.ForeignKey(Level, default=0)
    dept = models.ForeignKey(Dept, default=0)

    def __str__(self):
        return str(self.code) + ' ' + str(self.title)


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
    type = models.CharField(max_length=2, choices=type_choices, default='')
    sex = models.CharField(max_length=10, choices=sex_choices, default='')

    def __str__(self):
        return str(self.last_name) + ", " + str(self.first_name) + " " + str(self.username)


@receiver(pre_save, sender='core.User')
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
    college = models.ForeignKey(College)

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
        ('1', 'Professor'),
        ('2', 'Associate Professor'),
        ('3', 'Senior Lecturer'),
        ('4', 'Lecturer I'),
        ('5', 'Lecturer II'),
        ('6', 'Assistant Lecturer'),
        ('7', 'Graduate Assistant'),
    )
    status_choices = (
        ('1', 'Permanent'),
        ('2', 'Adjunct'),
    )
    user = models.OneToOneField(User, default=0)
    address = models.TextField(default='')
    phone = models.CharField(max_length=15, default='')
    rank = models.CharField(max_length=2, choices=rank_choices, default='')
    status = models.CharField(max_length=2, choices=status_choices, default='')
    dept = models.ForeignKey(Dept, default=0)

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
    )
    user = models.OneToOneField(User)
    phone = models.CharField(max_length=20, default='')
    dateBirth = models.DateField()
    nationality = models.CharField(max_length=20, default='')
    stateOrigin = models.CharField(max_length=20, default='')
    lga = models.CharField(max_length=20, default='')
    religion = models.CharField(max_length=20, default='')
    address = models.TextField(default='')
    nextKin = models.TextField(default='')
    nextKinAddress = models.TextField(default='')
    town = models.TextField(default='')
    genotype = models.CharField(max_length=5, choices=genotype_choices, default='')
    bloodGroup = models.CharField(max_length=5, choices=bloodGroup_choices, default='')
    parentNo = models.CharField(max_length=15, default=0)
    oLevel = models.CharField(max_length=15, choices=olevel_choices, default='')
    major = models.ForeignKey(Major, default=0)
    level = models.ForeignKey(Level, default=0)
    modeOfEntry = models.ForeignKey(ModeOfEntry, default=0)
    status = models.CharField(max_length=15, choices=status_choices, default=1)
    img = models.FileField()

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
    if kwargs['instance'].type == '7':
        student = Student.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
