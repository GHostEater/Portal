from rest_framework import serializers
from accounts.models import User, Student, CollegeOfficer, StudentAffairs, Lecturer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'type',
            'sex',
        ]


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
        fields = [
            'id',
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'type',
            'sex',
        ]
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
    user = serializers.SerializerMethodField()
    college = serializers.SerializerMethodField()
    collegeId = serializers.CharField(read_only=True)

    class Meta:
        model = CollegeOfficer
        fields = [
            'id',
            'user',
            'college',
            'collegeId',
        ]

    def get_user(self, obj):
        user = User.objects.get(pk=obj.user.id)
        user_s = UserSerializer(user).data
        return user_s

    def get_college(self, obj):
        return str(obj.college.name)

    def get_collegeId(self, obj):
        return str(obj.college.id)


class StudentAffairsSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = StudentAffairs
        fields = [
            'id',
            'user',
            'rank',
        ]

    def get_user(self, obj):
        user = User.objects.get(pk=obj.user.id)
        user_s = UserSerializer(user).data
        return user_s


class LecturerSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    dept = serializers.SerializerMethodField()
    deptId = serializers.SerializerMethodField()
    college = serializers.SerializerMethodField()

    class Meta:
        model = Lecturer
        fields = [
            'id',
            'user',
            'address',
            'phone',
            'rank',
            'status',
            'dept',
            'deptId',
            'college'
        ]

    def get_user(self, obj):
        user = User.objects.get(pk=obj.user.id)
        user_s = UserSerializer(user).data
        return user_s

    def get_dept(self, obj):
        return str(obj.dept.name)

    def get_deptId(self, obj):
        return str(obj.dept.id)

    def get_college(self, obj):
        return str(obj.dept.college.name)


class StudentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    major = serializers.SerializerMethodField()
    majorId = serializers.SerializerMethodField()
    levelId = serializers.SerializerMethodField()
    dept = serializers.SerializerMethodField()
    deptId = serializers.SerializerMethodField()
    college = serializers.SerializerMethodField()
    level = serializers.SerializerMethodField()
    modeOfEntry = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = [
            'id',
            'user',
            'phone',
            'dateBirth',
            'nationality',
            'stateOrigin',
            'lga',
            'religion',
            'address',
            'nextKin',
            'nextKinAddress',
            'town',
            'genotype',
            'bloodGroup',
            'parentNo',
            'oLevel',
            'status',
            'img',
            'level',
            'levelId',
            'major',
            'majorId',
            'dept',
            'deptId',
            'college',
            'modeOfEntry'
        ]

    def get_user(self, obj):
        user = User.objects.get(pk=obj.user.id)
        user_s = UserSerializer(user).data
        return user_s

    def get_major(self, obj):
        return str(obj.major.name)

    def get_majorId(self, obj):
        return str(obj.major.id)

    def get_levelId(self, obj):
        return str(obj.level.id)

    def get_dept(self, obj):
        return str(obj.major.dept.name)

    def get_deptId(self, obj):
        return str(obj.major.dept.id)

    def get_college(self, obj):
        return str(obj.major.dept.college.name)

    def get_level(self, obj):
        return str(obj.level.level)

    def get_modeOfEntry(self, obj):
        return str(obj.modeOfEntry.name)


class StudentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
