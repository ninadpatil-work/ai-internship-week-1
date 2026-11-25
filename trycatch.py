# 1
# import json
# from pathlib import Path


# def load_json_safely(file_path: Path) -> dict:
#     """Load a JSON file and handle common file or parsing errors."""
#     data: dict = {}
#     try:
#         with file_path.open(mode="r", encoding="utf-8") as f:
#             data = json.load(f)
#     except FileNotFoundError:
#         print(f"File not found: {file_path}. Returning empty config.")
#     except json.JSONDecodeError as exc:
#         print(f"Invalid JSON in {file_path} (line {exc.lineno}): {exc.msg}")
#     else:
#         print(f"Successfully loaded {len(data)} top-level keys from {file_path.name}.")
#     finally:
#         print(f"Finished load attempt for: {file_path}")
#     return data

# if __name__ == "__main__":
#     test_path = Path("sample_config.json")
#     result = load_json_safely(test_path)
#     print("Returned data:", result)



# 2
# raw_score = "7"  

# try:
#     score = float(raw_score)
# except (ValueError, TypeError):
#     score = 0.0

# print(f"Parsed score: {score}")



# 3
# def set_model_params(temperature: float, max_tokens: int) -> dict[str, float | int]:
#     """Validate and return generation parameters."""
#     if not isinstance(temperature, (int, float)) or isinstance(temperature, bool):
#         raise TypeError("temperature must be a numeric value.")
#     if not (0.0 <= temperature <= 2.0):
#         raise ValueError(f"temperature must be between 0.0 and 2.0, got {temperature}.")
#     if max_tokens <= 0:
#         raise ValueError(f"max_tokens must be greater than 0, got {max_tokens}.")

#     return {"temperature": float(temperature), "max_tokens": max_tokens}





# 4
# def set_model_params(temperature: float, max_tokens: int) -> dict[str, float | int]:
#     """Validate and return generation parameters."""
#     if not isinstance(temperature, (int, float)) or isinstance(temperature, bool):
#         raise TypeError("temperature must be a numeric value.")
#     if not (0.0 <= temperature <= 2.0):
#         raise ValueError(f"temperature must be between 0.0 and 2.0, got {temperature}.")
#     if max_tokens <= 0:
#         raise ValueError(f"max_tokens must be greater than 0, got {max_tokens}.")

#     return {"temperature": float(temperature), "max_tokens": max_tokens}


# def run_param_checks() -> None:
#     test_cases = [
#         (0.2, 512),     # Valid
#         (2.5, 256),     # Out-of-range temperature -> ValueError
#         (0.7, -10),     # Invalid max_tokens -> ValueError
#         ('0.5', 128),   # Wrong type -> TypeError
#         (True, 128),    # bool is a subclass of int in Python -> TypeError
#     ]

#     for temp, tokens in test_cases:
#         try:
#             params = set_model_params(temp, tokens)
#             print(f"Valid config for ({temp!r}, {tokens!r}): {params}")
#         except (TypeError, ValueError) as exc:
#             print(f"Rejected ({temp!r}, {tokens!r}): {type(exc).__name__} - {exc}")


# if __name__ == "__main__":
#     run_param_checks()