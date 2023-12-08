from django.shortcuts import render
import requests
import json
# # import request
# import datetime


# Create your views here.
def get_weather(city):
    weather_url = "https://api.openweathermap.org/data/2.5/weather"
    api_key ="9e8bcb7dbefe6026f04f1a997c7de70e"
    Params = {
        'q' : city,
        'appid': api_key,
        'units' : 'metric'
    }
    response = requests.get(weather_url, params=Params)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def home(request):
    city = request.GET.get('city')
    icon_url = "https://openweathermap.org/img/wn/10d@2x.png"
    if city:
        weather_data_result = get_weather(city)
        if weather_data_result is not None:
            # weather_data = json.dumps(weather_data_result, indent=4)
            #extracting details
            weather = weather_data_result['weather'][0]['main']
            weather_description = weather_data_result['weather'][0]['description']
            city = weather_data_result['name']
            country = weather_data_result['sys']['country']
            wind_speed = weather_data_result['wind']['speed']
            pressure = weather_data_result['main']['pressure']
            humidity = weather_data_result['main']['humidity']
            temperature = weather_data_result['main']['temp']
            icon_id = weather_data_result['weather'][0]['icon']
            icon_url = f"https://openweathermap.org/img/wn/{icon_id}@2x.png"


            return render(request, 'index.html', {
                'weather': weather,
                'weather_description': weather_description,
                'city': city,
                'country': country,
                'wind_speed': wind_speed,
                'pressure': pressure,
                'humidity': humidity,
                'temperature': temperature,
                'icon_url': icon_url,
            })

        else:
            return render(request, 'index.html')



    return render(request, 'index.html')