from rest_framework import serializers

from courseresulteditrequest.models import Request, Log


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'
        depth = 3

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.select_related(
            'lecturer',
            'lecturer__user',
            'handled_by',
        )
        return queryset


class RequestCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = '__all__'
        depth = 5

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.select_related(
            'result',
            'result__course',
            'result__course__level',
            'result__course__dept',
            'result__course__dept__college',
            'result__student',
            'result__student__user',
            'result__student__major',
            'result__student__major__dept',
            'result__student__major__dept__college',
            'result__student__level',
            'result__student__mode_of_entry',
            'result__dept',
            'result__dept__college',
            'result__session',
            'edited_by',
            'edited_by__user',
            'edited_by__dept',
            'edited_by__dept__college',
        )
        return queryset


class LogCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = '__all__'
