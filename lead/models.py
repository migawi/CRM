from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Lead(models.Model):
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'

    CHOICES_PRIORITY = (
        (LOW, 'Low'),
        (MEDIUM, 'Medium'),
        (HIGH, 'High'),
    )

    NEW = 'new'
    LOST = 'lost'
    WON = 'won'
    CONTACTED = 'contacted'

    CHOICES_STATUS = (
        (NEW, 'New'),
        (LOST, 'Lost'),
        (WON, 'Won'),
        (CONTACTED, 'Contacted'),
    )

    name = models.CharField(max_length=200)
    email = models.EmailField()
    definition = models.TextField(blank=True, null=True)
    priority = models.CharField(max_length=12, choices=CHOICES_PRIORITY, default=MEDIUM)
    status = models.CharField(max_length=12, choices=CHOICES_STATUS, default=NEW)

    created_by = models.ForeignKey(User, related_name='leads', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name