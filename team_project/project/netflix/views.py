# Create your views here.
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from .models import Subscription, SubscriptionPlan, Movie, Payment
from django.contrib import messages  
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('choose-subscription.html')  # Redirect to subscription selection page
        return render(request, 'register.html', {'form': form})

class ChooseSubscriptionView(View):
    def get(self, request):
        plans = SubscriptionPlan.objects.all()
        return render(request, 'choose-subscription.html', {'plans': plans})

class PaymentView(View):
    def post(self, request):
        # Handle payment processing logic here
        # Assuming payment processing is done successfully
        plan_id = request.POST.get('plan_id')
        plan = SubscriptionPlan.objects.get(id=plan_id)
        Subscription.objects.create(user=request.user, plan=plan)
        return redirect('login.html')  # Redirect to login page after successful payment

class ManageSubscriptionsView(View):
    @login_required
    def get(self, request):
        user_subscriptions = Subscription.objects.filter(user=request.user)
        return render(request, 'manage_subscriptions.html', {'user_subscriptions': user_subscriptions})

class UserPageView(View):
    @login_required
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




# class RegisterView(View):
#     def get(self, request):
#         form = UserCreationForm()
#         return render(request, 'register.html', {'form': form})

#     def post(self, request):
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}!')
#             return redirect('choose_subscription')  # Redirect to subscription selection page
#         return render(request, 'register.html', {'form': form})

# class SubscribeView(View):
#     def post(self, request):
#         plan_id = request.POST.get('plan_id')
#         plan = SubscriptionPlan.objects.get(id=plan_id)
#         # Process subscription and payment here
#         # Assuming payment processing is done and subscription is created successfully
#         Subscription.objects.create(user=request.user, plan=plan)
#         return redirect('login')  # Redirect to login page after subscription

# class ManageSubscriptionsView(View):
#     @login_required
#     def get(self, request):
#         user_subscriptions = Subscription.objects.filter(user=request.user)
#         return render(request, 'manage_subscriptions.html', {'user_subscriptions': user_subscriptions})

# class UserPageView(View):
#     @login_required
#     def get(self, request):
#         user = request.user
#         subscription = Subscription.objects.filter(user=user).first()
#         movies = Movie.objects.all()  # Adjust this query to filter movies based on user's subscription, if needed
#         context = {
#             'user': user,
#             'subscription': subscription,
#             'movies': movies
#         }
#         return render(request, 'user_page.html', context)


class HomeView(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UserCreationForm()  # Include the UserCreationForm for sign up
        return context

# # class ManageSubscriptionsView(View):
# #     def get(self, request):
# #         user_subscriptions = Subscription.objects.filter(user=request.user)
# #         return render(request, 'manage_subscriptions.html', {'user_subscriptions': user_subscriptions})

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
        return redirect('manage_subscriptions.html')
    
# # class UserPageView(View):
# #     def get(self, request):
# #         user = request.user
# #         subscription = Subscription.objects.filter(user=user).first()
# #         movies = Movie.objects.all()  # Adjust this query to filter movies based on user's subscription, if needed
# #         context = {
# #             'user': user,
# #             'subscription': subscription,
# #             'movies': movies
# #         }
# #         return render(request, 'user_page.html', context)

# # class RegisterView(View):
# #     def get(self, request):
# #         form = UserCreationForm()
# #         return render(request, 'register.html', {'form': form})

# #     def post(self, request):
# #         form = UserCreationForm(request.POST)
# #         if form.is_valid():
# #             form.save()
# #             username = form.cleaned_data.get('username')
# #             messages.success(request, f'Account created for {username}!')
# #             return redirect('login')  # Redirect to login page after successful registration
# #         return render(request, 'register.html', {'form': form})


class CustomLoginView(LoginView):

    @login_required
    # def get_success_url(self):
    #     # Redirect to the subscription page after successful login
    #     return '/choose-subscription.html/'
  
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