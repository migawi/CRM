from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Strategy(models.Model):
    name = models. CharField(max_length=100)
    definition = models.TextField()
    price = models.IntegerField()
    max_clients = models.IntegerField()
    max_leads = models.IntegerField()

    def __str__(self):
        return self.name

class Team(models.Model):
    strategy = models.ForeignKey(Strategy, related_name='teams', on_delete=models.CASCADE)
    name = models.CharField(max_length=90)
    members = models.ManyToManyField(User, related_name='teams')
    created_by = models.ForeignKey(User, related_name='created_teams', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
