from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)
    date = models.DateField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title