from django.db import models
from django.utils.text import slugify
from django.core.validators import RegexValidator
from account.models import StudentProfile


def get_resource_upload_path(instance, filename):
    return '{}/{}'.format(slugify(instance.__class__.__name__), filename)


class Resource(models.Model):
    file = models.FileField(upload_to=get_resource_upload_path)

    class Meta:
        abstract = True


class Book(Resource):
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50, blank=True, null=True)


class Notes(Resource):
    author = models.ForeignKey(StudentProfile, on_delete=models.SET_NULL, null=True, blank=True)
    topic = models.CharField(max_length=100, blank=True, null=True)


class Assignment(Resource):
    name = models.CharField(max_length=30, blank=True, null=True)


class QuestionPaper(Resource):
    # Validators
    YEAR_REGEX = RegexValidator(r'^[0-9]{4}$', message='Not a valid year!')
    # Choices
    EXAM_CHOICES = (
        ('MS1', 'Mid Sem 1'),
        ('MS2', 'Mid Sem 2'),
        ('ESM', 'End Sem')
    )
    # Model
    exam = models.CharField(max_length=3, choices=EXAM_CHOICES)
    year = models.PositiveIntegerField(validators=[YEAR_REGEX])


class Quiz(Resource):
    # Validators
    YEAR_REGEX = RegexValidator(r'^[0-9]{4}$', message='Not a valid year!')
    # Model
    year = models.PositiveIntegerField(validators=[YEAR_REGEX])
