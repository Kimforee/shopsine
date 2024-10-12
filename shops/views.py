from django.shortcuts import render, redirect
from .forms import ShopRegistrationForm
from .models import Shop
from .utils import haversine

def register_shop(request):
    if request.method == 'POST':
        form = ShopRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop_success')
    else:
        form = ShopRegistrationForm()
    
    return render(request, 'shops/register_shop.html', {'form': form})

def shop_success(request):
    return render(request, 'shops/success.html')

def search_shops(request):
    if request.method == 'POST':
        latitude = float(request.POST.get('latitude'))
        longitude = float(request.POST.get('longitude'))
        
        # fetch all shops from the database
        shops = Shop.objects.all()

        # calculate distances
        shop_distances = []
        for shop in shops:
            distance = haversine(latitude, longitude, shop.latitude, shop.longitude)
            shop_distances.append((shop, distance))
        
        # sort shops by distance
        sorted_shops = sorted(shop_distances, key=lambda x: x[1])

        return render(request, 'shops/search_results.html', {'shops': sorted_shops, 'user_lat': latitude, 'user_lon': longitude})
    
    return render(request, 'shops/search_shops.html')

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ShopSerializer

@api_view(['POST'])
def register_shop_api(request):
    if request.method == 'POST':
        serializer = ShopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Shop
from .serializers import ShopSerializer
from .utils import haversine

@api_view(['GET'])
def search_shops_api(request):
    try:
        latitude = float(request.GET.get('latitude'))
        longitude = float(request.GET.get('longitude'))
    except (TypeError, ValueError):
        return Response({"error": "Invalid latitude or longitude"}, status=status.HTTP_400_BAD_REQUEST)
    
    # fetch all shops and calculate distances
    shops = Shop.objects.all()
    shop_distances = []
    for shop in shops:
        distance = haversine(latitude, longitude, shop.latitude, shop.longitude)
        shop_distances.append((shop, distance))

    # sort by distance
    sorted_shops = sorted(shop_distances, key=lambda x: x[1])
    sorted_shop_data = [{'shop': ShopSerializer(shop).data, 'distance': distance} for shop, distance in sorted_shops]
    return Response(sorted_shop_data, status=status.HTTP_200_OK)