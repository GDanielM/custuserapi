from django.urls import path
from .views import SignupView, ProfileView

urlpatterns = [
    path('signup/',SignupView.as_view()),
    path('image/',ProfileView.as_view()),
]