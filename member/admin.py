from django.contrib import admin
from .models import Grade, Position, Member

admin.site.register(Position)
admin.site.register(Member)

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('name', )

