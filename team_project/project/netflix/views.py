# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from .models import Subscription, SubscriptionPlan, Movie, Payment
from django.contrib import messages  

class HomeView(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UserCreationForm()  # Include the UserCreationForm for sign up
        return context

class ManageSubscriptionsView(View):
    def get(self, request):
        user_subscriptions = Subscription.objects.filter(user=request.user)
        return render(request, 'manage_subscriptions.html', {'user_subscriptions': user_subscriptions})

class ManageMoviesView(View):
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, 'movies_page.html', {'movies': movies})

class SubscribeView(View):
    def post(self, request):
        plan_id = request.POST.get('plan_id')
        plan = SubscriptionPlan.objects.get(id=plan_id)
        # Process subscription and payment here
        # Assuming payment processing is done and subscription is created successfully
        Subscription.objects.create(user=request.user, plan=plan)
        return redirect('manage_subscriptions')

class AvailablePlansView(View):
    def get(self, request):
        plans = SubscriptionPlan.objects.all()
        return render(request, 'available_plans.html', {'plans': plans})

class ProcessPaymentView(View):
    def post(self, request):
        # Handle payment processing logic here
        # Assuming payment processing is done successfully
        amount = request.POST.get('amount')
        payment_method = request.POST.get('payment_method')
        transaction_id = '123456'  # Dummy transaction ID for demonstration
        Payment.objects.create(user=request.user, amount=amount, payment_method=payment_method, transaction_id=transaction_id, status='success')
        return redirect('manage_subscriptions')
    
class UserPageView(View):
    def get(self, request):
        user = request.user
        subscription = Subscription.objects.filter(user=user).first()
        movies = Movie.objects.all()  # Adjust this query to filter movies based on user's subscription, if needed
        context = {
            'user': user,
            'subscription': subscription,
            'movies': movies
        }
        return render(request, 'user_page.html', context)

