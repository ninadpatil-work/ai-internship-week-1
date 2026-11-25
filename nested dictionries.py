evaluation_runs = {
    "run_01": {
        "prompt_version": "v1.0",
        "metrics": {"accuracy": 0.84, "latency_ms": 310},
        "passed": True,
    },
    "run_02": {
        "prompt_version": "v1.1",
        "metrics": {"accuracy": 0.91, "latency_ms": 265},
        "passed": True,
    },
}

acc_run_02 = evaluation_runs["run_02"]["metrics"]["accuracy"]  # 0.91

# Safe nested lookup when an intermediate key might be missing
safe_latency = (
    evaluation_runs
    .get("run_03", {})
    .get("metrics", {})
    .get("latency_ms", -1)
)
print(safe_latency)  # -1

# Updating a nested metric
evaluation_runs["run_01"]["metrics"]["accuracy"] = 0.87


import copy

base_config = {"model": "base-llm", "params": {"temperature": 0.7, "max_tokens": 256}}

shallow = base_config.copy()
deep = copy.deepcopy(base_config)

shallow["params"]["temperature"] = 0.1  # Mutates `base_config["params"]` as well!
deep["params"]["max_tokens"] = 512      # Does NOT affect `base_config`

print(base_config["params"])            # {'temperature': 0.1, 'max_tokens': 256}