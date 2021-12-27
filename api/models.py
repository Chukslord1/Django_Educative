from django.db import models

# Create your models here.
class UserProfile(models.Model):
    name = models.TextField()
    age = models.IntegerField()
    phone = models.CharField(max_length=200)

    def __str__(self):
        return self.name