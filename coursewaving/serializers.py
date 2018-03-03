from rest_framework import serializers

from coursewaving.models import WavedCourses


class WavedCoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = WavedCourses
        fields = '__all__'
        depth = 4

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.select_related(
            'course',
            'course__dept',
            'course__dept__college',
            'course__level',
            'student',
            'student__user',
            'student__major',
            'student__major__dept',
            'student__major__dept__college',
            'student__level',
            'student__mode_of_entry',
            'waved_by',
            'waved_by__user',
            'waved_by__dept',
            'waved_by__dept__college',
        )
        return queryset


class WavedCoursesCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = WavedCourses
        fields = '__all__'
