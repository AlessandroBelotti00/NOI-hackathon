import requests
import datetime
import pandas as pd

def get_weather_data(api_key, city, date_time):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "dt": int(date_time.timestamp())  # Convert the datetime to UNIX timestamp
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error in the request: {response.status_code}")
        return None

# Replace "YOUR_API_KEY" with your OpenWeatherMap API key
api_key = "fa21783c20d87aa29a921bf628b0380f"

# Specify the city and the date range for which you want to get the weather data
city = "Trani"
start_date = datetime.datetime(2018, 8, 1)
end_date = datetime.datetime(2019, 8, 1)

# Create an empty list to store the weather data for each date
weather_data_list = []

# Loop through the date range and fetch weather data for each date
current_date = start_date
while current_date <= end_date:
    weather_data = get_weather_data(api_key, city, current_date)
    if weather_data:
        weather_data_list.append(weather_data)
    current_date += datetime.timedelta(days=1)

# Check if there is any data and then save it to a CSV file
if weather_data_list:
    # Convert the list of dictionaries into a pandas DataFrame
    df = pd.DataFrame(weather_data_list)

    # Specify the file name
    file_name = 'weather_data.csv'

    # Save data into CSV file
    df.to_csv(file_name, index=False)

    print(f'Data saved to {file_name}')