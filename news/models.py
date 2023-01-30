from django.db import models

class Item(models.Model):
    title = models.CharField(max_length=20)
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.title} - {self.name}"

