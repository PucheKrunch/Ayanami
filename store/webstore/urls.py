from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('login/',views.user_login, name='login'),
    path('register/',views.register, name='register'),
    path('cart/<str:pk>/',views.cart, name='cart'),
]