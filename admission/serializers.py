from rest_framework import serializers
from admission.models import Pin, Application


class PinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pin
        fields = '__all__'
        depth = 2

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.select_related(
            'application',
            'application__session',
        )
        return queryset


class PinCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pin
        fields = '__all__'


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'
        depth = 3

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.select_related(
            'session',
            'level',
            'choice',
            'choice__dept',
            'choice__dept__college',
        )
        return queryset


class ApplicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'
