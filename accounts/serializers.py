from rest_framework import serializers
from accounts.models import User, Student, CollegeOfficer, StudentAffairs, Lecturer, Dean, Unit


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        depth = 2


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'


class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False, allow_blank=True)
    email = serializers.CharField(required=False, allow_blank=True, read_only=True)
    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(allow_blank=True, read_only=True)
    last_name = serializers.CharField(allow_blank=True, read_only=True)
    type = serializers.CharField(allow_blank=True, read_only=True)
    sex = serializers.CharField(allow_blank=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        user_obj = None
        username = data['username']
        password = data['password']
        if not username:
            raise serializers.ValidationError('Username required to Login')

        user = User.objects.get(username__iexact=username)
        if user:
            user_obj = user
        else:
            raise serializers.ValidationError('This username is not valid')

        if user_obj:
            if not user_obj.check_password(password):
                raise serializers.ValidationError('Password is Incorrect')
        return user_obj


class CollegeOfficerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollegeOfficer
        fields = '__all__'
        depth = 2

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.select_related(
            'user',
            'college',
        )
        return queryset


class StudentAffairsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAffairs
        fields = '__all__'
        depth = 2

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.select_related(
            'user',
        )
        return queryset


class LecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecturer
        fields = '__all__'
        depth = 3

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.select_related(
            'user',
            'dept',
            'dept__college',
        )
        return queryset


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        depth = 3

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.select_related(
            'user',
            'major',
            'major__dept',
            'major__dept__college',
            'level',
            'mode_of_entry',
        )
        return queryset


class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class DeanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dean
        fields = '__all__'
        depth = 2

    @staticmethod
    def setup_eager_loading(queryset):
        queryset = queryset.select_related(
            'user',
            'college',
        )
        return queryset
