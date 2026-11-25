import json
from pathlib import Path

config_data = {
    "project": "ai-internship",
    "day": 4,
    "model_settings": {
        "temperature": 0.2,
        "max_tokens": 512,
        "stream": True,
    },
    "tags": ["python", "json", "file-io"],
    "notes": None,
}

output_dir = Path("day4_practice")
output_dir.mkdir(parents=True, exist_ok=True)
config_path = output_dir / "config.json"

with config_path.open(mode="w", encoding="utf-8") as f:
    json.dump(config_data, f, indent=2)


import json
from pathlib import Path

config_path = Path("day4_practice") / "config.json"

with config_path.open(mode="r", encoding="utf-8") as f:
    loaded_config = json.load(f)

print(type(loaded_config))                      # <class 'dict'>
print(loaded_config["project"])                   # ai-internship
print(loaded_config["model_settings"]["temperature"])  # 0.2