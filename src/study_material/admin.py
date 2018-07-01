from django.contrib import admin
from .models import Books, Assignment, Notes, PreviousYearQuizAndAssignments, PreviousYearSemPapers


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    class Meta:
        model = Books
        fields = '__all__'


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    class Meta:
        model = Assignment
        fields = '__all__'


@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    class Meta:
        model = Notes
        fields = '__all__'


@admin.register(PreviousYearQuizAndAssignments)
class PreviousYearQuizAndAssignmentsAdmin(admin.ModelAdmin):
    class Meta:
        model = PreviousYearQuizAndAssignments
        fields = '__all__'


@admin.register(PreviousYearSemPapers)
class PreviousYearSemPapersAdmin(admin.ModelAdmin):
    class Meta:
        model = PreviousYearSemPapers
        fields = '__all__'
