from django.db import models
from django.contrib.auth.models import User
from members.models import Club


class Association(models.Model):
    name = models.CharField(max_length=255, null=True, unique=True)
    type = models.CharField(max_length=255, null=True)
    headquarters = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class AssociationStaff(models.Model):
    association_id = models.ForeignKey(Association, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.association_id.name


class Membership(models.Model):
    association_id = models.ForeignKey(Association, on_delete=models.CASCADE)
    club_id = models.ForeignKey(Club, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, null=True)


class Subscription(models.Model):
    membership_id = models.ForeignKey(Membership, on_delete=models.CASCADE)
    club_id = models.ForeignKey(Club, on_delete=models.CASCADE)
    status = models.CharField(max_length=255, null=True)
    start_date = models.DateField()
    end_date = models.DateField()


class Event(models.Model):
    association_id = models.ForeignKey(Association, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True)
    date = models.DateField()
    description = models.CharField(max_length=255, null=True)
