
from django.urls import path
from . import views
from .views import ProduceView,ProfileView

# app_name will help us do a reverse look-up latter.
urlpatterns = [
  path('',views.welcome,name='Welcome'),
  path('search/', views.search_results, name='search_results'),
  path('buy/', views.display_all_produce, name='buy'),
  path('sell/', views.sell, name='sell'),
  path('profile/',views.display_profile,name='profile'),
  path('produce/', ProduceView.as_view()),
  path('profiles/',ProfileView.as_view()),
  path('<slug:slug>/', views.post_detail, name='post_detail')
#     path('profile/<int:pk>',ProduceView.as_view()),
#     path('produce/<int:pk>',ProduceView.as_view()),
  ]
