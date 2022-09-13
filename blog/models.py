from statistics import mode
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title