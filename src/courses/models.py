from django.db import models
from django.core.validators import RegexValidator
from account.models import FacultyProfile


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
    practicals = models.PositiveIntegerField()

    def __str__(self):
        return 'LTP ({}-{}-{})'.format(self.lectures, self.tutorials, self.practicals)


class Course(models.Model):
    # Validators
    code_regex = RegexValidator(r'^[A-Z]{2}[0-9]{3}')
    # Models
    code = models.CharField(max_length=5, validators=[code_regex])
    name = models.CharField(max_length=80)
    faculty = models.ForeignKey(FacultyProfile, on_delete=models.SET_NULL, null=True, blank=True)
    syllabus = models.TextField()
    marks_distribution = models.ForeignKey(MarksDistribution, on_delete=models.SET_NULL, blank=True, null=True)
    credit_distribution = models.ForeignKey(CreditDistribution, on_delete=models.SET_NULL, blank=True, null=True)
