from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model):
    AUTHOR = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    TITLE = models.CharField(max_length=200)
    TEXT = models.TextField()
    CREATED_ON = models.DateTimeField(default=timezone.now)
    PUBLISHED_ON = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.PUBLISHED_ON=timezone.now()
        self.save()


    def __str__(self):
        return self.TITLE