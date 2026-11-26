import json
from pathlib import Path
import requests


def fetch_and_save_weather(output_file: str = "mumbai_weather.json") -> None:
  url = "https://api.open-meteo.com/v1/forecast"
  params = {
      "latitude": 19.0760,
      "longitude": 72.8777,
      "current": "temperature_2m,wind_speed_10m,relative_humidity_2m",
      "timezone": "Asia/Kolkata",
  }

  try:
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    output_path = Path(output_file)
    with output_path.open("w", encoding="utf-8") as file:
      json.dump(data, file, indent=4, ensure_ascii=False)

    print(f"Data saved successfully to {output_path.resolve()}")

  except requests.exceptions.Timeout:
    print("Request timed out.")
  except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error: {http_err}")
  except requests.exceptions.RequestException as req_err:
    print(f"Request failed: {req_err}")
  except OSError as io_err:
    print(f"File write error: {io_err}")


if __name__ == "__main__":
  fetch_and_save_weather()