from fetch_and_save import fetch_and_save_weather

# Option A: Use default filename ("mumbai_weather.json")
success = fetch_and_save_weather()

# Option B: Save to a custom filename or subfolder
# success = fetch_and_save_weather("data/today_weather.json")

if success:
  print("Ready to process the saved JSON file.")
else:
  print("Skipping processing because fetch failed.")