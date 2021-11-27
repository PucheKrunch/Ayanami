from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('login/',views.user_login, name='login'),
    path('logout/',views.user_logout, name='logout'),
    path('register/',views.register, name='register'),
    path('cart/',views.cart, name='cart'),
    path('checkout/',views.checkout, name='checkout'),
    path('updateItem/',views.updateItem, name='updateItem'),
    path('processOrder/',views.processOrder, name='processOrder'),
    path('guest/',views.guest, name='guest'),
    path('search/',views.search, name='search'),
    path('apanel/',views.apanel, name='apanel'),
    path('addproduct/',views.add_product, name='addproduct'),
    path('product/<str:pk>/',views.product_page, name='product_page'),
]