from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Volunteer(models.Model):
    vol_number = models.IntegerField(blank=False, null=False)
    lname = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    vol_dob = models.DateTimeField(
        default=timezone.now)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    email = models.EmailField(max_length=200)
    cell_phone = models.CharField(max_length=50)
    vol_notes = models.CharField(max_length=50)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)


    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.vol_number)


class Inventory(models.Model):
    donor = models.CharField(max_length=50)
    item_code = models.IntegerField(primary_key=True,blank=False, null=False)
    item_name = models.CharField(primary_key=True,max_length=200)
    item_quantity = models.IntegerField(blank=False)
    acquired_date = models.DateField(default=timezone.now)

    def created(self):
        self.acquired_date = timezone.now()
        self.save()


class Client(models.Model):
    client_ID = models.IntegerField(blank=False, null=False)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    age = models.IntegerField(blank=False, null=False)
    client_dob = models.DateField(
        default=timezone.now)
    gender = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    created_date = models.DateField(
        default=timezone.now)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.client_ID)



