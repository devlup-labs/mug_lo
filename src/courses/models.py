from django.db import models
from django.core.validators import RegexValidator
from accounts.models import FacultyProfile


class MarksDistribution(models.Model):
    mid_sem_1 = models.PositiveIntegerField()
    mid_sem_2 = models.PositiveIntegerField()
    end_sem = models.PositiveIntegerField()
    lab = models.PositiveIntegerField()
    assignments = models.PositiveIntegerField()
    quiz = models.PositiveIntegerField()


class CreditDistribution(models.Model):
    lectures = models.PositiveIntegerField()
    tutorials = models.PositiveIntegerField()
    lab = models.PositiveIntegerField()


class Course(models.Model):
    # Validators
    code = RegexValidator(r'^[A-Z]{2}[0-9]{3}')
    # Models
    course_code = models.CharField(max_length=5, validators=[code])
    course_name = models.CharField(max_length=80)
    faculty = models.ForeignKey(FacultyProfile, on_delete=models.SET_NULL, null=True, blank=True)
    syllabus = models.TextField()
    marks_distribution = models.ForeignKey(MarksDistribution, on_delete=models.SET_NULL, blank=True, null=True)
    credit_distribution = models.ForeignKey(CreditDistribution, on_delete=models.SET_NULL, blank=True, null=True)
