from django.urls import path
from .views import HomeView, ManageSubscriptionsView, ChooseSubscriptionView, ManageMoviesView, SubscribeView, AvailablePlansView, ProcessPaymentView, UserPageView, RegisterView, CustomLoginView

app_name='netflix'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('manage_subscriptions/', ManageSubscriptionsView.as_view(), name='manage_subscriptions'),
    path('manage_movies/', ManageMoviesView.as_view(), name='manage_movies'),
    path('subscribe/', SubscribeView.as_view(), name='subscribe'),
    path('available_plans/', AvailablePlansView.as_view(), name='available_plans'),
    path('process_payment/', ProcessPaymentView.as_view(), name='process_payment'),
    path('user_page/', UserPageView.as_view(), name='user_page'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('choose-subscription/', ChooseSubscriptionView.as_view(), name='choose_subscription')
]



# urlpatterns = [
#     path('home/', HomeView.as_view(), name='main'),
#     path('subscriptions/', ManageSubscriptionsView.as_view(), name='manage_subscriptions'),
#     path('movies/', ManageMoviesView.as_view(), name='movies_page'),
#     path('subscribe/', SubscribeView.as_view(), name='subscribe'),
#     path('available-plans/', AvailablePlansView.as_view(), name='available_plans'),
#     path('process-payment/', ProcessPaymentView.as_view(), name='process_payment'),
#     path('user/', UserPageView.as_view(), name='user_page'),
#     # path('login/', UserPageView.as_view(template_name='main.html'), name='login'),
#     path('register/', RegisterView.as_view(), name='register'),
# ]

