import requests
from django.contrib import messages
from django.shortcuts import render

def index(request):
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=bca4a874f27d33fe4bd0dadd4d83ead6'
	#city = 'London'

	if request.method == 'POST':

			city = request.POST['cityName']
			r = requests.get(url.format(city)).json()
			print(r)
			if r['cod'] == 200:				
				city_weather = {
					'city': city,
					'temperature': r['main']['temp'],
					'description': r['weather'][0]['description'],
					'icon': r['weather'][0]['icon'],
				}
				return render(request, 'core/base.html',{'city_weather':city_weather})
			else:
				messages.info(request, "Please enter a valid city name")

	return render(request,'core/base.html')

	#r = requests.get(url.format(city))
	#print(r.text)

	# r = requests.get(url.format(city)).json()		
	# city_weather = {
	# 	'city': city,
	# 	'temperature': r['main']['temp'],
	# 	'description': r['weather'][0]['description'],
	# 	'icon': r['weather'][0]['icon'],
	# }

	# #print(city_weather)
	# context = {'city_weather' : city_weather}
	# return render(request, 'core/base.html', context)
