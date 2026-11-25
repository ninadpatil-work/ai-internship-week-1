# Writing text (overwrites the file if it already exists)
with open("prompt_notes.txt", mode="w", encoding="utf-8") as file:
    file.write("System Prompt: Be concise and accurate.\n")
    file.write("Temperature: 0.2\n")

# Reading the entire file as a single string
with open("prompt_notes.txt", mode="r", encoding="utf-8") as file:
    content = file.read()

print(content)


with open("run_log.txt", mode="a", encoding="utf-8") as log_file:
    log_file.write("Run completed: status=OK\n")


with open("run_log.txt", mode="r", encoding="utf-8") as log_file:
    for line_number, line in enumerate(log_file, start=1):
        clean_line = line.rstrip("\r\n")
        print(f"Line {line_number}: {clean_line}")


from pathlib import Path

output_dir = Path("day4_practice")
output_dir.mkdir(parents=True, exist_ok=True)

notes_path = output_dir / "sample_notes.txt"
notes_path.write_text("Day 4: File I/O started.\n", encoding="utf-8")

loaded_text = notes_path.read_text(encoding="utf-8")
print(loaded_text)