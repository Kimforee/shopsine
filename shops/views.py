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
        
        # Fetch all shops from the database
        shops = Shop.objects.all()

        # Calculate distances
        shop_distances = []
        for shop in shops:
            distance = haversine(latitude, longitude, shop.latitude, shop.longitude)
            shop_distances.append((shop, distance))
        
        # Sort shops by distance
        sorted_shops = sorted(shop_distances, key=lambda x: x[1])

        return render(request, 'shops/search_results.html', {'shops': sorted_shops, 'user_lat': latitude, 'user_lon': longitude})
    
    return render(request, 'shops/search_shops.html')