import openmeteo_requests

import pandas as pd
import requests_cache
from retry_requests import retry

def previsao_temperatura(latitude, longitude):

    # Setup the Open-Meteo API client with cache and retry on error
    cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
    retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
    openmeteo = openmeteo_requests.Client(session = retry_session)

    # Make sure all required weather variables are listed here
    # The order of variables in hourly or daily is important to assign them correctly below
    url = "https://api.open-meteo.com/v1/forecast"
    # -23.446977060290134, -46.918508019295224 fábrica de programadores
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m",
    }
    responses = openmeteo.weather_api(url, params = params)

    # Process first location. Add a for-loop for multiple locations or weather models
    response = responses[0]
    print(f"Coordinates: {response.Latitude()}°N {response.Longitude()}°E")
    print(f"Elevation: {response.Elevation()} m asl")
    print(f"Timezone difference to GMT+0: {response.UtcOffsetSeconds()}s")

    # Process hourly data. The order of variables needs to be the same as requested.
    hourly = response.Hourly()
    hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()

    hourly_data = {
        "date": pd.date_range(
            start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
            end =  pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
            freq = pd.Timedelta(seconds = hourly.Interval()),
            inclusive = "left"
        )
    }

    hourly_data["temperature_2m"] = hourly_temperature_2m

    hourly_dataframe = pd.DataFrame(data = hourly_data)
    print("\nHourly data\n", hourly_dataframe)

    dias_semana = {
    0 : 'Segunda-feira',
    1 : 'Terça-feira',
    2 : 'Quarta-feira',
    3 : 'Quinta-feira',
    4 : 'Sexta-feira',
    5 : 'Sábado',
    6 : 'Domingo'
    }

    hourly_dataframe['dia'] = hourly_dataframe['date'].apply(lambda x: x.day)
    hourly_dataframe['mes'] = hourly_dataframe['date'].apply(lambda x: x.month)
    hourly_dataframe['dia_semana'] = hourly_dataframe['date'].apply(lambda x: x.weekday()).map(dias_semana)

    temperatura_media = hourly_dataframe.groupby(['dia', 'mes','dia_semana'])['temperature_2m'].mean().reset_index()
    temperatura_media.columns = ['dia', 'mes','dia_semana', 'temperatura_media']

    return hourly_dataframe, temperatura_media