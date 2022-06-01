from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *


# Register your models here.



@admin.register(Category_Course)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title",)
    list_filter = ("title",)
    search_fields = ("title",)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "category_course")
    list_filter = ("title", "category_course")
    search_fields = ("title", "category_course", "description", "stepic_link", "udemy_link", "my_link")


admin.site.register(User_Account)