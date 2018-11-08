from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from coursereview.models import CourseReview


class CourseReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseReview
        fields = '__all__'
        depth = 4

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.select_related(
            'course',
            'course__level',
            'course__dept',
            'course__dept__college',
            'student',
            'student__user',
            'student__major',
            'student__major__dept',
            'student__major__dept__college',
            'student__level',
            'student__mode_of_entry',
            'lecturer',
            'lecturer__dept',
            'lecturer__dept__college',
            'session',
        )
        return queryset


class CourseReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        validators = [
            UniqueTogetherValidator(
                queryset=CourseReview.objects.all(),
                fields=('student', 'course', 'session', 'lecturer')
            )
        ]
        model = CourseReview
        fields = '__all__'
