
from django.urls import path

from .views import ProduceView,ProfileView


app_name = "marketplace"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('produce/', ProduceView.as_view()),
    path('profiles/',ProfileView.as_view()),
    path('profile/<int:pk>',ProduceView.as_view()),
    path('produce/<int:pk>',ProduceView.as_view()),
]