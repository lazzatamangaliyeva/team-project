from django.contrib import admin
from .models import *

admin.site.register(SubscriptionPlan)
admin.site.register(Subscription)
admin.site.register(Movie)
admin.site.register(Category)
admin.site.register(Payment)

