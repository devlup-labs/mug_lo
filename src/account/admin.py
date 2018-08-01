from django.contrib import admin
from .models import StudentProfile, FacultyProfile


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    class Meta:
        model = StudentProfile
        fields = '__all__'


@admin.register(FacultyProfile)
class FacultyProfileAdmin(admin.ModelAdmin):
    class Meta:
        model = FacultyProfile
        fields = '__all__'
