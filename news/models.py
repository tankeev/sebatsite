from django.db import models
from django.utils import timezone


class News(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now())
    photo = models.FileField(upload_to='media/', blank=True)
    hight_field=models.IntegerField(default=0)
    width_field=models.IntegerField(default=0)

    def publish(self):
        self.date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Event(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()
	date = models.DateTimeField()
	photo = models.ImageField()