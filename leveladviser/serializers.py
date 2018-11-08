from rest_framework import serializers
from leveladviser.models import LevelAdviser


class LevelAdviserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LevelAdviser
        fields = '__all__'
        depth = 3

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.select_related(
            'lecturer',
            'lecturer__user',
            'lecturer__dept',
            'lecturer__dept__college',
            'major',
            'major__dept',
            'major__dept__college',
        )
        queryset = queryset.prefetch_related('level')
        return queryset


class LevelAdviserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LevelAdviser
        fields = '__all__'
