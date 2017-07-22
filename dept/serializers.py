from rest_framework import serializers
from dept.models import Dept


class DeptSerializer(serializers.ModelSerializer):
    college = serializers.SerializerMethodField()

    class Meta:
        model = Dept
        fields = [
            'id',
            'name',
            'college',
        ]

    def get_college(self, obj):
        return str(obj.college.name)
