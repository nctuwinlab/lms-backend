from django.contrib import admin
from .models import Store, Food

# Register your models here.


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)


class FoodAdminInline(admin.TabularInline):
    model = Food
    extra = 1


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'note',)
    inlines = (FoodAdminInline,)
