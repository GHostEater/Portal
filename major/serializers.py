from rest_framework import serializers
from major.models import Major


class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = '__all__'
        depth = 3

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.select_related(
            'dept',
            'dept__college',
        )
        return queryset
