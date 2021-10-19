from django.urls import path
from users import views

urlpatterns = [
    path('register/', views.user_register, name='user_register'),
]
