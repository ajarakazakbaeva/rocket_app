from django.contrib.auth.models import User
from django.db import models

class Courier(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(blank=True)
    phone_number = models.TextField(blank=True)

    def __str__(self):
        return self.user.__str__()

