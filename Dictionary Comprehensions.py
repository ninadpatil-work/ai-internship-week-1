models = ["gpt-4o-mini", "gemini-2.5-flash", "llama-3-8b"]
name_lengths = {model: len(model) for model in models}
print(name_lengths)
# {'gpt-4o-mini': 11, 'gemini-2.5-flash': 16, 'llama-3-8b': 10}


latencies_ms = {
    "retriever": 85,
    "reranker": 140,
    "llm_call": 620,
    "logger": 12,
}

# Keep only slow steps (> 100 ms) and convert ms to seconds
slow_steps_sec = {
    step: round(ms / 1000, 3)
    for step, ms in latencies_ms.items()
    if ms > 100
}
print(slow_steps_sec)  # {'reranker': 0.14, 'llm_call': 0.62}


role_codes = {"admin": 1, "editor": 2, "viewer": 3}
code_to_role = {code: role for role, code in role_codes.items()}
print(code_to_role)  # {1: 'admin', 2: 'editor', 3: 'viewer'}