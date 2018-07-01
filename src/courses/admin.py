from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    class Meta:
        model = Course
        fields = '__all__'
