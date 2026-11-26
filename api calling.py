import requests


def fetch_location_weather():
  url = "https://api.open-meteo.com/v1/forecast"
  params = {"latitude": 36, "longitude": 80, "current_weather": True}

  try:
    response = requests.get(url, params=params, timeout=10)
    # Raises an HTTPError if the status code is 4xx or 5xx
    response.raise_for_status()

    data = response.json()
    current = data.get("current_weather",{})

    print(f"Temperature: {current.get('temperature')} °C")
    print(f"Wind Speed:  {current.get('windspeed')} km/h")
    print(f"Time (UTC):  {current.get('time')}")

  except requests.exceptions.Timeout:
    print("Request timed out. Please try again.")
  except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
  except requests.exceptions.RequestException as err:
    print(f"Network or request error: {err}")


if __name__ == "__main__":
  fetch_location_weather()