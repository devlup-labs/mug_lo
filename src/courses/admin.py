from django.contrib import admin
from .models import Course, MarksDistribution, CreditDistribution
from courses.forms import MarksDistributionForm


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    class Meta:
        model = Course
        fields = '__all__'


@admin.register(MarksDistribution)
class MarksDistributionAdmin(admin.ModelAdmin):
    form = MarksDistributionForm

    class Meta:
        model = MarksDistribution
        fields = '__all__'


@admin.register(CreditDistribution)
class CreditDistributionAdmin(admin.ModelAdmin):
    class Meta:
        model = CreditDistribution
        fields = '__all__'
