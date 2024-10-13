from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_shop, name='register_shop'),
    path('success/', views.shop_success, name='shop_success'),
    path('search/', views.search_shops, name='search_shops'),
    path('api/register/', views.register_shop_api, name='register_shop_api'),
    path('api/search/', views.search_shops_api, name='search_shops_api'),
]