# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from coursereview.serializers import CourseReviewSerializer, CourseReviewCreateSerializer
from coursereview.models import CourseReview

# Create your views here.


class CourseReviewAPIView(ListAPIView):
    serializer_class = CourseReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = CourseReview.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class CourseReviewCreateAPIView(CreateAPIView):
    serializer_class = CourseReviewCreateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = CourseReview.objects.all()
        return queryset


class CourseReviewStudentAPIView(ListAPIView):
    serializer_class = CourseReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = CourseReview.objects.filter(student=self.request.GET['student'])
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class CourseReviewLecturerAPIView(ListAPIView):
    serializer_class = CourseReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = CourseReview.objects.filter(lecturer=self.request.GET['lecturer'])
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class CourseReviewCourseAPIView(ListAPIView):
    serializer_class = CourseReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = CourseReview.objects.filter(
            course=self.request.GET['course'],
            session=self.request.GET['session'])
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


class CourseReviewDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CourseReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = CourseReview.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset
