from rest_framework import serializers
from latereg.models import RegStatus, LateReg, Log


class RegStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegStatus
        fields = "__all__"


class LateRegSerializer(serializers.ModelSerializer):
    class Meta:
        model = LateReg
        fields = "__all__"
        depth = 4

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.select_related(
            'student',
            'student__user',
            'student__major',
            'student__major__dept',
            'student__major__dept__college',
            'student__level',
            'student__mode_of_entry',
            'session',
        )
        return queryset


class LateRegCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LateReg
        fields = "__all__"


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = "__all__"
        depth = 4

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.select_related(
            'student',
            'student__user',
            'student__major',
            'student__major__dept',
            'student__major__dept__college',
            'student__level',
            'student__mode_of_entry',
            'approved_by',
        )
        return queryset


class LogCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = "__all__"
