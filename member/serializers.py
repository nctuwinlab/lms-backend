from django.contrib.auth.models import User
from django.contrib.auth.validators import UnicodeUsernameValidator

from rest_framework import serializers

from .models import Profile, Grade, Position


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        extra_kwargs = {
            'username': {
                'validators': [UnicodeUsernameValidator()],
            }
        }


class ProfileSerializer(serializers.ModelSerializer):

    user = UserSerializer()

    # User's Public information
    grade = serializers.PrimaryKeyRelatedField(queryset=Grade.objects.all())
    position = serializers.PrimaryKeyRelatedField(
                            queryset=Position.objects.all())
    github = serializers.CharField(max_length=20, allow_blank=True)

    # User's Personal information (but visible by others)
    student_id = serializers.CharField(max_length=7, allow_blank=True)
    birth = serializers.DateField()
    mobile = serializers.CharField(max_length=10)
    website = serializers.URLField(allow_blank=True)

    # User's Private information (only visible by advisor)
    address = serializers.CharField(max_length=100, allow_blank=True)
    telphone = serializers.CharField(max_length=10, allow_blank=True)

    def __unicode__(self):
        return self.chinese_name

    def create(self, validated_data):
        username = validated_data.get('user').get('username')

        user = User.objects.create_user(
            username=username,
            password=self.generate_password(username),
            email=validated_data.get('user').get('email'),
            first_name=validated_data.get('user').get('first_name'),
            last_name=validated_data.get('user').get('last_name'),
        )

        validated_data.pop('user')

        profile = Profile.objects.create(user=user, **validated_data)
        return profile

    def update(self, instance, validated_data):

        # User can only change following attributes
        instance.grade = validated_data.get('grade', instance.grade)
        instance.position = validated_data.get('position', instance.position)
        instance.github = validated_data.get('github', instance.github)
        instance.mobile = validated_data.get('mobile', instance.mobile)
        instance.website = validated_data.get('website', instance.website)
        instance.address = validated_data.get('address', instance.address)
        instance.telphone = validated_data.get('telphone', instance.telphone)
        instance.save()

        return instance

    def generate_password(self, username):
        return username[::-1]

    class Meta:
        model = Profile
        fields = ['user', 'grade', 'position', 'github', 'student_id',
                  'birth', 'mobile', 'website', 'address', 'telphone']


class GradeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=5, default='使用者年級')
    profiles = serializers.PrimaryKeyRelatedField(
                many=True, read_only=True
            )

    def __unicode__(self):
        return self.name

    class Meta:
        model = Grade
        fields = ('name', 'profiles')


class Position(serializers.ModelSerializer):
    name = serializers.CharField(max_length=5, default='使用者職位')
    profiles = serializers.PrimaryKeyRelatedField(
                many=True, read_only=True
            )

    def __unicode__(self):
        return self.name

    class Meta:
        model = Position
        fields = ['name', 'profiles']
