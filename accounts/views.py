# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import IntegrityError
from django.db.models import Q
from django.http import JsonResponse
from django.template.loader import get_template
from mailqueue.models import MailerMessage
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from accounts.serializers import (
    UserSerializer,
    UserLoginSerializer,
    StudentSerializer,
    CollegeOfficerSerializer,
    StudentAffairsSerializer,
    LecturerSerializer,
    DeanSerializer,
    UnitSerializer,
    BursarSerializer)
from accounts.models import Student, User, CollegeOfficer, StudentAffairs, Lecturer, Dean, Unit, Bursar
from courseresultgpa.models import CourseResultGPA
from systemlog.models import Log
from level.models import Level
from modeofentry.models import ModeOfEntry
from major.models import Major

# Create your views here.


def current_user(request):
    user = request.user
    serial = UserSerializer(user)
    return JsonResponse(serial.data, safe=False, status=200)


class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer

    @staticmethod
    def post(request, *args, **kwargs):
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


class UserEmailAPIView(RetrieveAPIView):
    serializer_class = UserSerializer
    lookup_field = 'email'

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


class BursarAPIView(ListAPIView):
    serializer_class = BursarSerializer
    queryset = Bursar.objects.all()


class BursarDetailAPIView(RetrieveUpdateAPIView):
    serializer_class = BursarSerializer
    lookup_field = 'user'
    queryset = Bursar.objects.all()


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


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def student_upload(request):
    data = request.data
    processed = 0

    for i, body in enumerate(data):
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
        try:
            user.save()
        except IntegrityError:
            user = User.objects.get(username=body['username'])

        student = Student()
        student.user = user
        student.major = major
        student.level = level
        student.mode_of_entry = mode_of_entry
        student.status = '1'
        student.parent_email = body['parent_email']
        try:
            student.save()
            processed = i
        except IntegrityError:
            student = ''

    return Response({'processed': processed})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def student_graduate(request):
    req = request.data

    for d in req:
        student = Student.objects.get(pk=d['id'])
        student.status = '8'
        student.save()

    return Response({})


@api_view(['GET'])
@permission_classes([AllowAny])
def student_auto_withdraw(request):
    students = Student.objects.filter(status='1')
    for student in students:
        gps = CourseResultGPA.objects.filter(student=student.id)
        count = 0
        i = 0
        for gp in gps:
            if float(gp.cgpa) < 1.00:
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
    return Response({})


@api_view(['POST'])
@permission_classes([AllowAny])
def pass_reset(request):
    req = request.data
    try:
        user = User.objects.get(Q(email__iexact=req['email']) | Q(username__iexact=req['email']))
        if user:
            user_exists = True
        else:
            user_exists = False
        link = req['link']

        template = get_template('pass_reset.html')
        context = {'link': link, 'user': user}
        content = template.render(context)

        message = MailerMessage()
        message.subject = str("Password Reset from " + req['school_med_name'])
        message.to_address = user.email
        message.bcc_address = req['sender_email']
        message.from_address = req['sender_email']
        message.content = ""
        message.html_content = content
        message.app = req['school_med_name'] + " Mailing System"
        message.save()
    except User.DoesNotExist:
        user_exists = False

    return Response({'user_exists': user_exists})
