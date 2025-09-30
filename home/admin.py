from django.contrib import admin
from .models import Level, Question, Course

@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # faqat mavjud maydonlar
    search_fields = ('name',)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'level', 'uz_text', 'en_text')
    list_filter = ('level',)
    search_fields = ('uz_text', 'en_text')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    search_fields = ('title', 'description')
# Agar kerak bo'lsa, boshqa modellarning admin interfeysini ham shu yerda sozlash mumkin