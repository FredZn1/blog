from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100),
    email = models.EmailField(unique=True),
    bio = models.TextField(blank=True, null=True),

    def __str__(self):
        return f"{self.name}"

