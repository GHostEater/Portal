from rest_framework import serializers

from courseallocation.models import CourseAllocation


class CourseAllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseAllocation
        fields = '__all__'
        depth = 3

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.select_related(
            'course',
            'course__level',
            'course__dept',
            'course__dept__college',
            'lecturer',
            'lecturer__user',
            'lecturer__dept',
            'lecturer__dept__college',
            'allocated_by',
            'allocated_by__user',
            'allocated_by__dept',
            'allocated_by__dept__college',
            'session',
            'dept',
            'dept__college',
        )
        return queryset


class CourseAllocationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseAllocation
        fields = '__all__'
