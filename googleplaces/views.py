from django.http import HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, redirect
from .models import Location
from .forms import LocationForm
import googlemaps
import time
from djgeojson.fields import PointField

API_KEY = 'AIzaSyAEgoK9e2B11QmFZRfpRW3fH9UwIOJf8pY'

GEO_KEY = 'AIzaSyAuQF_Xlk-l0DsWoDG3JG0na57bhtGchgI'

gmaps = googlemaps.Client(key = API_KEY)

geomaps = googlemaps.Client(key = GEO_KEY)

def index(request):
	if request.method == 'POST':
		print("posted")
		form = LocationForm(request.POST)
		if form.is_valid():
			print("valid")
			post = form.save(commit=False)
			address = form.cleaned_data['address']
			address_result = geomaps.geocode(address = address)
			lat_result = address_result[0]['geometry']['location']['lat']
			lng_result = address_result[0]['geometry']['location']['lng']
			coord = "{0}, {1}".format(float(lng_result), float(lat_result))
			print(coord)
			post.geom = {'type': 'Point', 'coordinates': [float(lng_result), float(lat_result)]}
			post.save()
			return redirect('results')
		else:
			print("invalid")
	else:
		form = LocationForm()

	template = loader.get_template('googleplaces/index.html')
	return render(request, 'googleplaces/index.html', {'form': form})

def results(request):
	locations = Location.objects.all()
	template = loader.get_template('googleplaces/results.html')
	return render(request, 'googleplaces/results.html', {'locations': locations})