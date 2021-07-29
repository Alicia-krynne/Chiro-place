
from django.urls import path
from . import views
from .views import ProduceView,ProfileView


app_name = "marketplace"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
  path('',views.welcome,name='Welcome'),
  # path('search/', views.search_results, name='search_results'),
  path('produce/', ProduceView.as_view()),
  path('profiles/',ProfileView.as_view()),
#     path('profile/<int:pk>',ProduceView.as_view()),
#     path('produce/<int:pk>',ProduceView.as_view()),
  ]