# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from accounts.serializers import (
    UserSerializer,
    UserLoginSerializer,
    StudentSerializer,
    CollegeOfficerSerializer,
    StudentAffairsSerializer,
    LecturerSerializer,
    DeanSerializer,
    UnitSerializer
)
from accounts.models import Student, User, CollegeOfficer, StudentAffairs, Lecturer, Dean, Unit
from courseresultgpa.models import CourseResultGPA
from systemlog.models import Log
from level.models import Level
from modeofentry.models import ModeOfEntry
from major.models import Major
import json
from django.views.decorators.csrf import csrf_exempt
import datetime

# Create your views here.


def current_user(request):
    user = request.user
    serial = UserSerializer(user)
    return JsonResponse(serial.data, safe=False, status=200)


class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class UserAPIView(ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all().exclude(type='7').exclude(type='1')
        return queryset


class UserDetailAPIView(RetrieveUpdateAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset


class UnitAPIView(ListAPIView):
    serializer_class = UnitSerializer

    def get_queryset(self):
        queryset = Unit.objects.all()
        return queryset


class UnitDetailAPIView(RetrieveUpdateAPIView):
    serializer_class = UnitSerializer

    def get_queryset(self):
        queryset = Unit.objects.all()
        return queryset


class CollegeOfficerAPIView(ListAPIView):
    serializer_class = CollegeOfficerSerializer

    def get_queryset(self):
        queryset = CollegeOfficer.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class CollegeOfficerDetailAPIView(RetrieveUpdateAPIView):
    serializer_class = CollegeOfficerSerializer
    lookup_field = 'user'

    def get_queryset(self):
        queryset = CollegeOfficer.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class StudentAffairsAPIView(ListAPIView):
    serializer_class = StudentAffairsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = StudentAffairs.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class StudentAffairsDetailAPIView(RetrieveUpdateAPIView):
    serializer_class = StudentAffairsSerializer
    lookup_field = 'user'

    def get_queryset(self):
        queryset = StudentAffairs.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class LecturerAPIView(ListAPIView):
    serializer_class = LecturerSerializer

    def get_queryset(self):
        queryset = Lecturer.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class LecturerDetailAPIView(RetrieveUpdateAPIView):
    serializer_class = LecturerSerializer
    lookup_field = 'user'

    def get_queryset(self):
        queryset = Lecturer.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class DeanAPIView(ListAPIView):
    serializer_class = DeanSerializer
    queryset = Dean.objects.all()


class DeanDetailAPIView(RetrieveUpdateAPIView):
    serializer_class = DeanSerializer
    lookup_field = 'user'

    def get_queryset(self):
        queryset = Dean.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class StudentAPIView(ListAPIView):
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Student.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class StudentDeptAPIView(ListAPIView):
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Student.objects.filter(major__dept=self.request.GET['dept'])
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class StudentDetailAPIView(RetrieveUpdateAPIView):
    serializer_class = StudentSerializer
    lookup_field = 'user'

    def get_queryset(self):
        queryset = Student.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


@csrf_exempt
def student_create(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    major = Major.objects.get(name=body['major'])
    level = Level.objects.get(level=body['level'])
    mode_of_entry = ModeOfEntry.objects.get(name=body['mode_of_entry'])
    date_birth = body['date_birth']

    user = User()
    user.username = body['username']
    user.password = date_birth
    user.first_name = body['first_name']
    user.last_name = body['last_name']
    user.email = body['email']
    user.type = '7'
    user.sex = body['sex']
    user.date_birth = date_birth
    user.save()

    student = Student()
    student.user = user
    student.major = major
    student.level = level
    student.mode_of_entry = mode_of_entry
    student.status = '1'
    student.save()

    serial = StudentSerializer(student)
    return JsonResponse(serial.data, safe=False, status=200)


@csrf_exempt
def student_auto_withdraw(request):
    students = Student.objects.filter(status='1')
    for student in students:
        gps = CourseResultGPA.objects.filter(student=student.id)
        count = 0
        i = 0
        for gp in gps:
            if float(gp.cgpa) < 1.5:
                count += 1
            if count == 4:
                std = Student.objects.get(pk=student.id)
                std.status = '7'
                std.save()
                log = Log()
                log.action = "Withdraw Student " + std.user.username
                log.user = "System"
                log.role = "Super Admin"
                log.date = datetime.datetime.now()
                log.location = "System"
                log.save()
            i += 1
            if i == 2:
                continue
    return JsonResponse({}, safe=False, status=200)
