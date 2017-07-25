# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.contrib.auth.hashers import make_password

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
    LecturerSerializer
)
from accounts.models import Student, User, CollegeOfficer, StudentAffairs, Lecturer
from courseResultGpa.models import CourseResultGPA
from systemLog.models import Log
from level.models import Level
from modeOfEntry.models import ModeOfEntry
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


class CollegeOfficerAPIView(ListAPIView):
    serializer_class = CollegeOfficerSerializer
    permission_classes = [IsAuthenticated]
    queryset = CollegeOfficer.objects.all()


class CollegeOfficerDetailAPIView(RetrieveUpdateAPIView):
    serializer_class = CollegeOfficerSerializer
    lookup_field = 'user'
    queryset = CollegeOfficer.objects.all()


class StudentAffairsAPIView(ListAPIView):
    serializer_class = StudentAffairsSerializer
    permission_classes = [IsAuthenticated]
    queryset = StudentAffairs.objects.all()


class StudentAffairsDetailAPIView(RetrieveUpdateAPIView):
    serializer_class = StudentAffairsSerializer
    lookup_field = 'user'
    queryset = StudentAffairs.objects.all()


class LecturerAPIView(ListAPIView):
    serializer_class = LecturerSerializer
    permission_classes = [IsAuthenticated]
    queryset = Lecturer.objects.all()


class LecturerDetailAPIView(RetrieveUpdateAPIView):
    serializer_class = LecturerSerializer
    lookup_field = 'user'
    queryset = Lecturer.objects.all()


class StudentAPIView(ListAPIView):
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Student.objects.all()


class StudentDeptAPIView(ListAPIView):
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Student.objects.filter(major__dept=self.request.GET['dept'])


class StudentDetailAPIView(RetrieveUpdateAPIView):
    serializer_class = StudentSerializer
    lookup_field = 'user'
    queryset = Student.objects.all()


@csrf_exempt
def student_create(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)

    major = Major.objects.get(name=body['major'])
    level = Level.objects.get(level=body['level'])
    modeOfEntry = ModeOfEntry.objects.get(name=body['modeOfEntry'])
    dateBirth = body['dateBirth']

    user = User()
    user.username = body['username']
    user.password = dateBirth
    user.first_name = body['first_name']
    user.last_name = body['last_name']
    user.email = body['email']
    user.type = '7'
    user.sex = body['sex']
    user.save()

    student = Student()
    student.user = user
    student.major = major
    student.level = level
    student.modeOfEntry = modeOfEntry
    student.status = '1'
    student.dateBirth = dateBirth
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
                std.status = 6
                std.save()
                log = Log()
                log.action = "Withdraw Student " + std.user.username
                log.user = "System"
                log.role = "Super Admin"
                log.date = datetime.datetime.now()
                log.location = "System"
                log.save()
            i += 1
            if i == 3:
                continue
        return JsonResponse({}, safe=False, status=200)
