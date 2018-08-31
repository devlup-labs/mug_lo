from django.contrib import admin
from .models import Book, Assignment, Notes, Quiz, QuestionPaper


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    class Meta:
        model = Book
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


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    class Meta:
        model = Quiz
        fields = '__all__'


@admin.register(QuestionPaper)
class QuestionPaperAdmin(admin.ModelAdmin):
    class Meta:
        model = QuestionPaper
        fields = '__all__'
