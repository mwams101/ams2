from django.db import models
from django.contrib.auth.models import User


class Club(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class ClubStaff(models.Model):
    club_id = models.ForeignKey(Club, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=255, null=True)
