from django.shortcuts import render
from django.views import View
import urllib
from estate.models import Office


# Create your views here.
class MapsStatic(View):

    def get(self, request):
        offices = Office.objects.all()

        for office in offices:
            api_key = "AIzaSyDNOmIANiGAchyRd4y9KPIU1VYRPuSF5po"
            center = f'{office.geo_lat},{office.geo_long}'
            size = '600x600'
            format = 'png'
            zoom = 'zoom=13'
            markers = f'size:big,color:EE7E35|{office.geo_lat},{office.geo_long}'
            map_type = 'maptype=hybrid'
            url = f"https://maps.googleapis.com/maps/api/staticmap?center={center}&zoom={zoom}&size={size}&maptype={map_type}&key={api_key}&format={format}&markers={markers}"

            print(url)

        return render(request, 'static.html', {'offices': offices})
