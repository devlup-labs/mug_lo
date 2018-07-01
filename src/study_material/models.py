from django.db import models
from django.core.validators import RegexValidator
from accounts.models import StudentProfile


class Books(models.Model):
    book_name = models.CharField(max_length=50)
    file = models.FileField(upload_to='books')
    author = models.CharField(max_length=50, blank=True, null=True)


class Notes(models.Model):
    author = models.ForeignKey(StudentProfile, on_delete=models.SET_NULL, null=True, blank=True)
    topic = models.CharField(max_length=100, blank=True, null=True)
    file = models.FileField(upload_to='notes')


class Assignment(models.Model):
    assignment_name = models.CharField(max_length=30, blank=True, null=True)
    file = models.FileField(upload_to='assignment')


class PreviousYearSemPapers(models.Model):
    # Validators
    valid_year = RegexValidator(r'^[0-9]{4}$', message='Not a valid year!')
    # Model
    year = models.PositiveIntegerField(validators=[valid_year])
    file = models.FileField(upload_to='previous-year-papers')
    mid_sem_1 = models.BooleanField()
    mid_sem_2 = models.BooleanField()
    end_sem = models.BooleanField()


class PreviousYearQuizAndAssignments(models.Model):
    # Validators
    valid_year = RegexValidator(r'^[0-9]{4}$', message='Not a valid year!')
    # Model
    year = models.PositiveIntegerField(validators=[valid_year])
    file = models.FileField(upload_to='previous-year-papers')
