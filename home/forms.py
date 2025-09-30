from django import forms
from .models import Level, Question, Course, Video, Test

# =========================
# Level Form
# =========================
class LevelForm(forms.ModelForm):
    class Meta:
        model = Level
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Level nomi'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Level tavsifi', 'rows': 3}),
        }


# =========================
# Question Form
# =========================
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['level', 'text', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_option']
        widgets = {
            'level': forms.Select(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'option_a': forms.TextInput(attrs={'class': 'form-control'}),
            'option_b': forms.TextInput(attrs={'class': 'form-control'}),
            'option_c': forms.TextInput(attrs={'class': 'form-control'}),
            'option_d': forms.TextInput(attrs={'class': 'form-control'}),
            'correct_option': forms.Select(attrs={'class': 'form-control'}),
        }


# =========================
# Course Form
# =========================
class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }


# =========================
# Video Form
# =========================
class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['course', 'title', 'url', 'order']
        widgets = {
            'course': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'url': forms.URLInput(attrs={'class': 'form-control'}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
        }


# =========================
# Test Form
# =========================
class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['course', 'question', 'answer']
        widgets = {
            'course': forms.Select(attrs={'class': 'form-control'}),
            'question': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'answer': forms.TextInput(attrs={'class': 'form-control'}),
        }
# =========================