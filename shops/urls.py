from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_shop, name='register_shop'),
    path('success/', views.shop_success, name='shop_success'),
    path('search/', views.search_shops, name='search_shops'),
]