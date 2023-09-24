from django.db import models
from django.utils import timezone

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=122)  # Change this to EmailField for email addresses
    password = models.CharField(max_length=128)  # Change max_length to a more secure value (e.g., 128 for a hashed password)
    textarea = models.TextField(max_length=500)
    date = models.DateField()
    
    def __str__(self):
        return self.name + f' ({self.email})'
