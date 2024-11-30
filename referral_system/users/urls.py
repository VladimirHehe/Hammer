from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoginView, VerifyView, ProfileView, ActivateInviteView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('verify/', VerifyView.as_view(), name='verify'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='user-profile'),
    path('activate -invite/<int:pk>/', ActivateInviteView.as_view(), name='user-activate-invite'),
]
