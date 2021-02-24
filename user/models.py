from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

# Create your models here.
from django.urls import reverse


class CustomUser(AbstractUser):
    # add additional fields in here
    profile_id = models.CharField(default=uuid.uuid4(), max_length=150)

    def __str__(self):
        return str(self.profile_id)

    def can_view(self, obj):
        if obj.profile_id == self.profile_id:
            return True

    def get_absolute_url(self):
        return reverse("user:profile_detail", args=[str(self.profile_id)])
