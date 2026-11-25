raw_tags = ["  Python ", "", "SQL", "  rag  ", "   ", "Git "]

# Clean whitespace, drop empty strings, and normalize casing
clean_tags = [tag.strip().lower() for tag in raw_tags if tag.strip()]
print(clean_tags)  # ['python', 'sql', 'rag', 'git']