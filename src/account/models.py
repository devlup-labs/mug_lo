from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class StudentProfile(models.Model):
    # Validators
    roll = RegexValidator(r'^[BMP][0-9]{2}[A-Z]{2}[0-9]{3}')
    # Models
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_no = models.CharField(max_length=8, validators=[roll])
    courses = models.ManyToManyField('courses.Course', blank=True)


class FacultyProfile(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    office_address = models.TextField(null=True, blank=True)
