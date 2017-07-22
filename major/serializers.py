from rest_framework import serializers
from major.models import Major


class MajorSerializer(serializers.ModelSerializer):
    dept = serializers.SerializerMethodField()
    college = serializers.SerializerMethodField()

    class Meta:
        model = Major
        fields = [
            'id',
            'name',
            'dept',
            'college',
        ]

    def get_dept(self, obj):
        return str(obj.dept.name)

    def get_college(self, obj):
        return str(obj.dept.college.name)
