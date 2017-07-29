from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.models import User
from member.models import Grade, Position, Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    extra = 1


class UserAdmin(AuthUserAdmin):
    inlines = (ProfileInline, )


admin.site.register(Grade)
admin.site.register(Position)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
