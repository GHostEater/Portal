# -*- coding: utf-8 -*-
from __future__ import unicode_literals, division

from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from accounts.models import Student
from courseallocation.models import CourseAllocation
from courseallocation.serializers import CourseAllocationSerializer
from coursereg.models import CourseReg
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


class CourseReviewDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CourseReviewSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = CourseReview.objects.all()
        queryset = self.get_serializer_class().setup_eager_loading(queryset)
        return queryset


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def course_review_restrict(request):
    reviews = CourseReview.objects.filter(course__semester=request.GET['semester'],
                                          session=request.GET['session'],
                                          student=request.GET['student'])
    course_reg = CourseReg.objects.filter(course__semester=request.GET['semester'],
                                          session=request.GET['session'],
                                          student=request.GET['student'])
    done_reviews = False

    for course in course_reg:
        try:
            reviews.get(course=course.course)
            done_reviews = True
        except CourseReview.DoesNotExist:
            done_reviews = False

    if course_reg.count() == 0:
        done_reviews = True

    student = Student.objects.get(pk=request.GET['student'])
    if student.level.level == '100':
        done_reviews = True

    return Response({'done_reviews': done_reviews})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def course_review_student(request):
    req = request.GET

    response = []

    student = Student.objects.get(pk=req['student'])
    course_reg = CourseReg.objects.filter(student=req['student'],
                                          session=req['session'],
                                          course__semester=req['semester'])
    allocations = CourseAllocation.objects.filter(session=req['session'],
                                                  course__semester=req['semester'])
    for course in course_reg:
        try:
            lects = allocations.filter(course=course.course)

            for lect in lects:
                response.append(lect)

        except CourseAllocation.DoesNotExist:
            lects = CourseAllocation()

    return Response(CourseAllocationSerializer(response, many=True).data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def course_review_course(request):
    reviews = CourseReview.objects.filter(course=request.GET['course'],
                                          session=request.GET['session'],
                                          lecturer=request.GET['lecturer'])
    q1 = 0
    q2 = 0
    q3 = 0
    q4 = 0
    q5 = 0
    q6 = 0
    q7 = 0
    q8 = 0
    q9 = 0
    q10 = 0
    q11 = 0
    q12 = 0
    q13 = 0
    q14 = 0
    q15 = 0
    q16 = 0
    q17 = 0
    q18 = 0
    q19 = 0
    q20 = 0
    q21 = 0
    q22 = 0
    q23 = 0
    q24 = 0
    q25 = 0
    q26 = 0
    q27 = 0
    q28 = 0
    q29 = 0
    for review in reviews:
        q1 += review.q1
        q2 += review.q2
        q3 += review.q3
        q4 += review.q4
        q5 += review.q5
        q6 += review.q6
        q7 += review.q7
        q8 += review.q8
        q9 += review.q9
        q10 += review.q10
        q11 += review.q11
        q12 += review.q12
        q13 += review.q13
        q14 += review.q14
        q15 += review.q15
        q16 += review.q16
        q17 += review.q17
        q18 += review.q18
        q19 += review.q19
        q20 += review.q20
        q21 += review.q21
        q22 += review.q22
        q23 += review.q23
        q24 += review.q24
        q25 += review.q25
        q26 += review.q26
        q27 += review.q27
        q28 += review.q28
        q29 += review.q29

    if reviews.count() > 0:
        avg_q1 = q1 / reviews.count()
        avg_q2 = q2 / reviews.count()
        avg_q3 = q3 / reviews.count()
        avg_q4 = q4 / reviews.count()
        avg_q5 = q5 / reviews.count()
        avg_q6 = q6 / reviews.count()
        avg_q7 = q7 / reviews.count()
        avg_q8 = q8 / reviews.count()
        avg_q9 = q9 / reviews.count()
        avg_q10 = q10 / reviews.count()
        avg_q11 = q11 / reviews.count()
        avg_q12 = q12 / reviews.count()
        avg_q13 = q13 / reviews.count()
        avg_q14 = q14 / reviews.count()
        avg_q15 = q15 / reviews.count()
        avg_q16 = q16 / reviews.count()
        avg_q17 = q17 / reviews.count()
        avg_q18 = q18 / reviews.count()
        avg_q19 = q19 / reviews.count()
        avg_q20 = q20 / reviews.count()
        avg_q21 = q21 / reviews.count()
        avg_q22 = q22 / reviews.count()
        avg_q23 = q23 / reviews.count()
        avg_q24 = q24 / reviews.count()
        avg_q25 = q25 / reviews.count()
        avg_q26 = q26 / reviews.count()
        avg_q27 = q27 / reviews.count()
        avg_q28 = q28 / reviews.count()
        avg_q29 = q29 / reviews.count()
    else:
        avg_q1 = 0
        avg_q2 = 0
        avg_q3 = 0
        avg_q4 = 0
        avg_q5 = 0
        avg_q6 = 0
        avg_q7 = 0
        avg_q8 = 0
        avg_q9 = 0
        avg_q10 = 0
        avg_q11 = 0
        avg_q12 = 0
        avg_q13 = 0
        avg_q14 = 0
        avg_q15 = 0
        avg_q16 = 0
        avg_q17 = 0
        avg_q18 = 0
        avg_q19 = 0
        avg_q20 = 0
        avg_q21 = 0
        avg_q22 = 0
        avg_q23 = 0
        avg_q24 = 0
        avg_q25 = 0
        avg_q26 = 0
        avg_q27 = 0
        avg_q28 = 0
        avg_q29 = 0

    total = avg_q1 + avg_q2 + avg_q3 + avg_q4 + avg_q5 + avg_q6 + avg_q7 + avg_q8 + avg_q9 + avg_q10 + avg_q11 + avg_q12 + avg_q13 + avg_q14 + avg_q15 + avg_q16 + avg_q17 + avg_q18 + avg_q19 + avg_q20 + avg_q21 + avg_q22 + avg_q23 + avg_q24 + avg_q25 + avg_q26 + avg_q27 + avg_q28 + avg_q29

    total_percentage = float((total / 145) * 100)

    avg_scores = {
        'q1': avg_q1,
        'q2': avg_q2,
        'q3': avg_q3,
        'q4': avg_q4,
        'q5': avg_q5,
        'q6': avg_q6,
        'q7': avg_q7,
        'q8': avg_q8,
        'q9': avg_q9,
        'q10': avg_q10,
        'q11': avg_q11,
        'q12': avg_q12,
        'q13': avg_q13,
        'q14': avg_q14,
        'q15': avg_q15,
        'q16': avg_q16,
        'q17': avg_q17,
        'q18': avg_q18,
        'q19': avg_q19,
        'q20': avg_q20,
        'q21': avg_q21,
        'q22': avg_q22,
        'q23': avg_q23,
        'q24': avg_q24,
        'q25': avg_q25,
        'q26': avg_q26,
        'q27': avg_q27,
        'q28': avg_q28,
        'q29': avg_q29
    }

    data = {
        'reviews': CourseReviewSerializer(reviews, many=True).data,
        'avg_scores': avg_scores,
        'total': total,
        'total_percentage': total_percentage
    }

    return Response(data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def course_review_dept(request):
    req = request.GET
    data = []
    allocations = CourseAllocation.objects.filter(session=req['session'], dept=req['dept'])

    for alloc in allocations:
        reviews = CourseReview.objects.filter(course=alloc.course.id,
                                              course__semester=req['semester'],
                                              session=req['session'],
                                              lecturer=alloc.lecturer.id)
        if reviews.count() == 0:
            continue
        q1 = 0
        q2 = 0
        q3 = 0
        q4 = 0
        q5 = 0
        q6 = 0
        q7 = 0
        q8 = 0
        q9 = 0
        q10 = 0
        q11 = 0
        q12 = 0
        q13 = 0
        q14 = 0
        q15 = 0
        q16 = 0
        q17 = 0
        q18 = 0
        q19 = 0
        q20 = 0
        q21 = 0
        q22 = 0
        q23 = 0
        q24 = 0
        q25 = 0
        q26 = 0
        q27 = 0
        q28 = 0
        q29 = 0
        for review in reviews:
            q1 += review.q1
            q2 += review.q2
            q3 += review.q3
            q4 += review.q4
            q5 += review.q5
            q6 += review.q6
            q7 += review.q7
            q8 += review.q8
            q9 += review.q9
            q10 += review.q10
            q11 += review.q11
            q12 += review.q12
            q13 += review.q13
            q14 += review.q14
            q15 += review.q15
            q16 += review.q16
            q17 += review.q17
            q18 += review.q18
            q19 += review.q19
            q20 += review.q20
            q21 += review.q21
            q22 += review.q22
            q23 += review.q23
            q24 += review.q24
            q25 += review.q25
            q26 += review.q26
            q27 += review.q27
            q28 += review.q28
            q29 += review.q29

        if reviews.count() > 0:
            avg_q1 = q1 / reviews.count()
            avg_q2 = q2 / reviews.count()
            avg_q3 = q3 / reviews.count()
            avg_q4 = q4 / reviews.count()
            avg_q5 = q5 / reviews.count()
            avg_q6 = q6 / reviews.count()
            avg_q7 = q7 / reviews.count()
            avg_q8 = q8 / reviews.count()
            avg_q9 = q9 / reviews.count()
            avg_q10 = q10 / reviews.count()
            avg_q11 = q11 / reviews.count()
            avg_q12 = q12 / reviews.count()
            avg_q13 = q13 / reviews.count()
            avg_q14 = q14 / reviews.count()
            avg_q15 = q15 / reviews.count()
            avg_q16 = q16 / reviews.count()
            avg_q17 = q17 / reviews.count()
            avg_q18 = q18 / reviews.count()
            avg_q19 = q19 / reviews.count()
            avg_q20 = q20 / reviews.count()
            avg_q21 = q21 / reviews.count()
            avg_q22 = q22 / reviews.count()
            avg_q23 = q23 / reviews.count()
            avg_q24 = q24 / reviews.count()
            avg_q25 = q25 / reviews.count()
            avg_q26 = q26 / reviews.count()
            avg_q27 = q27 / reviews.count()
            avg_q28 = q28 / reviews.count()
            avg_q29 = q29 / reviews.count()
        else:
            avg_q1 = 0
            avg_q2 = 0
            avg_q3 = 0
            avg_q4 = 0
            avg_q5 = 0
            avg_q6 = 0
            avg_q7 = 0
            avg_q8 = 0
            avg_q9 = 0
            avg_q10 = 0
            avg_q11 = 0
            avg_q12 = 0
            avg_q13 = 0
            avg_q14 = 0
            avg_q15 = 0
            avg_q16 = 0
            avg_q17 = 0
            avg_q18 = 0
            avg_q19 = 0
            avg_q20 = 0
            avg_q21 = 0
            avg_q22 = 0
            avg_q23 = 0
            avg_q24 = 0
            avg_q25 = 0
            avg_q26 = 0
            avg_q27 = 0
            avg_q28 = 0
            avg_q29 = 0

        total = avg_q1 + avg_q2 + avg_q3 + avg_q4 + avg_q5 + avg_q6 + avg_q7 + avg_q8 + avg_q9 + avg_q10 + avg_q11 + avg_q12 + avg_q13 + avg_q14 + avg_q15 + avg_q16 + avg_q17 + avg_q18 + avg_q19 + avg_q20 + avg_q21 + avg_q22 + avg_q23 + avg_q24 + avg_q25 + avg_q26 + avg_q27 + avg_q28 + avg_q29

        total_percentage = float((total / 145) * 100)

        avg_scores = {
            'q1': avg_q1,
            'q2': avg_q2,
            'q3': avg_q3,
            'q4': avg_q4,
            'q5': avg_q5,
            'q6': avg_q6,
            'q7': avg_q7,
            'q8': avg_q8,
            'q9': avg_q9,
            'q10': avg_q10,
            'q11': avg_q11,
            'q12': avg_q12,
            'q13': avg_q13,
            'q14': avg_q14,
            'q15': avg_q15,
            'q16': avg_q16,
            'q17': avg_q17,
            'q18': avg_q18,
            'q19': avg_q19,
            'q20': avg_q20,
            'q21': avg_q21,
            'q22': avg_q22,
            'q23': avg_q23,
            'q24': avg_q24,
            'q25': avg_q25,
            'q26': avg_q26,
            'q27': avg_q27,
            'q28': avg_q28,
            'q29': avg_q29
        }

        d = {
            'alloc': CourseAllocationSerializer(alloc).data,
            'reviews': CourseReviewSerializer(reviews, many=True).data,
            'avg_scores': avg_scores,
            'total': total,
            'total_percentage': total_percentage
        }
        data.append(d)

    return Response(data)
