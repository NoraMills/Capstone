from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    # image = need to set up file upload system
    _id = models.AutoField(primary_key=True, editable=False)
    description = models.TextField(null=True, blank=True)
