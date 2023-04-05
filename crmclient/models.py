from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Client(models.Model):
    
    name = models.CharField(max_length=200)
    email = models.EmailField()
    definition = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='clients', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name