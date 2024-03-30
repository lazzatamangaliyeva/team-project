# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class SubscriptionPlan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration = models.CharField(max_length=50)  # e.g., Monthly, Yearly
    features = models.TextField()  # Features included in the plan

    def __str__(self):
        return self.name

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plan = models.ForeignKey(SubscriptionPlan, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('canceled', 'Canceled'), ('expired', 'Expired')])

    def __str__(self):
        return f"{self.user.username}'s {self.plan.name} Subscription"

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnails/')
    video_link = models.URLField(max_length=200, default = '') 
    upload_date = models.DateField(auto_now_add=True)
    duration = models.CharField(max_length=20)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=100)
    transaction_id = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=[('success', 'Success'), ('pending', 'Pending'), ('failed', 'Failed')])

    def __str__(self):
        return f"{self.user.username} - {self.amount} - {self.payment_date}"
