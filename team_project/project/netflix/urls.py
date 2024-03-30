from django.urls import path
from .views import HomeView, ManageSubscriptionsView, ManageMoviesView, SubscribeView, AvailablePlansView, ProcessPaymentView, UserPageView

urlpatterns = [
    path('home/', HomeView.as_view(), name='main'),
    path('subscriptions/', ManageSubscriptionsView.as_view(), name='manage_subscriptions'),
    path('movies/', ManageMoviesView.as_view(), name='movies_page'),
    path('subscribe/', SubscribeView.as_view(), name='subscribe'),
    path('available-plans/', AvailablePlansView.as_view(), name='available_plans'),
    path('process-payment/', ProcessPaymentView.as_view(), name='process_payment'),
    path('user/', UserPageView.as_view(), name='user_page'),
    path('login/', LoginView.as_view(template_name='main.html'), name='login'),
]

