from django.db import models
from django.contrib.auth.models import User


class Grade(models.Model):
    name = models.CharField(max_length=5, default='使用者年級')

    def __str__(self):
        return self.name


class Position(models.Model):
    name = models.CharField(max_length=5, default='使用者職位')

    def __str__(self):
        return self.name


class Profile(models.Model):
    # Using built-in auth model
    user = models.OneToOneField(User)

    # User's Public information
    grade = models.ForeignKey('Grade', blank=True)
    position = models.ForeignKey('Position', blank=True)
    github = models.CharField(max_length=20, blank=True)

    # User's Personal information (but visible by others)
    student_id = models.CharField(max_length=7, blank=True)
    birth = models.DateField(blank=True)
    mobile = models.CharField(max_length=10)
    website = models.URLField(blank=True)

    # User's Private information (only visible by advisor)
    address = models.CharField(max_length=100, blank=True)
    telphone = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.user.first_name
