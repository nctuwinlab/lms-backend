from django.contrib.auth.models import User

from rest_framework import serializers
from .models import Profile, Grade, Position


class UserSerializer(serializers.Serializer):
    profile = serializers.PrimaryKeyRelatedField(
                queryset=Profile.objects.all()
            )

    class Meta:
        model = User
        fields = ('id', 'username', 'profile')


class ProfileSerializer(serializers.Serializer):

    # User's Public information
    chinese_name = serializers.CharField(required=True, max_length=10)
    english_name = serializers.CharField(max_length=30, blank=True)
    grade = models.ForeignKey('Grade', blank=True)
    position = models.ForeignKey('Position', blank=True)
    github = models.CharField(max_length=20, blank=True)

    # User's Personal information (but visible by others)
    student_id = serializers.CharField(max_length=7, blank=True)
    email = serializers.EmailField()
    birth = serializers.DateField(blank=True)
    mobile = serializers.CharField(max_length=10)
    website = serializers.URLField(blank=True)

    # User's Private information (only visible by advisor)
    address = serializers.CharField(max_length=40, blank=True)
    telphone = serializers.CharField(max_length=10, blank=True)


class GradeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=5, default='使用者年級')
    profiles = serializers.PrimaryKeyRelatedField(
                many=True, read_only=True
            )

    class Meta:
        model = Grade
        fields = ('name', 'profiles')


class Position(models.Model):
    name = serializers.CharField(max_length=5, default='使用者職位')
    profiles = serializers.PrimaryKeyRelatedField(
                many=True, read_only=True
            )

    class Meta:
        model = Position
        fields = ('name', 'profiles')
