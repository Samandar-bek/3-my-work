from django.db import models

class Level(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# home/models.py
class Question(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name='questions')
    uz_text = models.CharField(max_length=255)
    en_text = models.CharField(max_length=255)
    order = models.PositiveIntegerField(default=0)  # bu qo‘shildi

    def __str__(self):
        return self.uz_text[:50]


    def __str__(self):
        return f"{self.level.name} - {self.uz_text[:20]}"

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title
class Video(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='videos')
    title = models.CharField(max_length=200)
    url = models.URLField()
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.course.title} - {self.title}"