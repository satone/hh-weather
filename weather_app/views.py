import requests, os
from django.http import JsonResponse, HttpResponse


def index(_):
    CITY = os.getenv('CITY', 'Moscow')
    base_url = 'https://geocoding-api.open-meteo.com/v1/'
    json_geo = requests.get(f'{base_url}search?name={CITY}').json()
    lat, lon = json_geo['results'][0]['latitude'], json_geo['results'][0]['longitude']
    url = f"{base_url}forecast?latitude={lat}&longitude={lon}&current_weather=true&temperature_unit=celsius"
    try:
        (response := requests.get(url)).raise_for_status()
        return HttpResponse(f"<h2>{response.json()['current_weather']['temperature']}</h2>")
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)
