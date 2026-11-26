import json
from pathlib import Path
import requests


def fetch_and_save_weather(output_file: str = "mumbai_weather.json") -> bool:
  url = "https://api.open-meteo.com/v1/forecast"
  params = {
      "latitude": 19.0760,
      "longitude": 72.8777,
      "current": "temperature_2m,wind_speed_10m,relative_humidity_2m",
      "timezone": "Asia/Kolkata",
  }

  try:
    response = requests.get(url, params=params, timeout=10)
    # Catch 4xx (client errors) and 5xx (server errors) as bad responses
    response.raise_for_status()
    data = response.json()

  except requests.exceptions.ConnectionError:
    print("No internet connection or unable to reach the server.")
    return False
  except requests.exceptions.Timeout:
    print("The request timed out. Try again in a moment.")
    return False
  except requests.exceptions.HTTPError as http_err:
    status = response.status_code if response is not None else "unknown"
    print(f"Bad response from server (HTTP {status}): {http_err}")
    return False
  except ValueError:
    # Covers requests.exceptions.JSONDecodeError (a subclass of ValueError)
    print("Received a response, but it was not valid JSON.")
    return False
  except requests.exceptions.RequestException as req_err:
    print(f"Unexpected network/request error: {req_err}")
    return False

  try:
    output_path = Path(output_file)
    with output_path.open("w", encoding="utf-8") as file:
      json.dump(data, file, indent=4, ensure_ascii=False)
    print(f"Data saved successfully to {output_path.resolve()}")
    return True
  except OSError as io_err:
    print(f"Failed to write JSON file: {io_err}")
    return False


if __name__ == "__main__":
  fetch_and_save_weather()