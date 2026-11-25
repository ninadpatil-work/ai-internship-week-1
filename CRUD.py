candidate = {
    "name": "Ninad Patil",
    "role": "AI Intern",
    "score": 88,
}

empty_dict = {}
from_pairs = dict([("model", "gemini"), ("top_k", 5)])


print(candidate["name"])                 # Ninad Patil
print(candidate.get("location", "N/A"))  # N/A (safe fallback)

# Checking keys, values, and pairs
print("score" in candidate)              # True
print(list(candidate.keys()))            # ['name', 'role', 'score']
print(list(candidate.values()))          # ['Ninad Patil', 'AI Intern', 88]
for key, value in candidate.items():
    print(f"{key}: {value}")


candidate["score"] = 92                 # Update existing key
candidate["city"] = "Thane"             # Add new key

candidate.update({"score": 95, "level": "Intermediate"})
candidate.setdefault("attempts", 1)     # Sets 1 only if "attempts" is not already present



removed_level = candidate.pop("level", None)  # Removes key and returns value (or None if absent)
del candidate["city"]                          # Removes key; raises KeyError if missing
last_key, last_val = candidate.popitem()       # Removes and returns the last inserted (key, value) pair
# candidate.clear()                            # Empties the entire dictionary