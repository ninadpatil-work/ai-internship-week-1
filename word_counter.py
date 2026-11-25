import string


def normalize_text(text: str) -> list[str]:
    """Lowercase text, strip punctuation from tokens, and return non-empty words."""
    tokens = text.lower().split()
    cleaned_words: list[str] = []

    for token in tokens:
        word = token.strip(string.punctuation)
        if word:
            cleaned_words.append(word)

    return cleaned_words


def count_word_frequencies(text: str) -> dict[str, int]:
    """Return a dictionary mapping each normalized word to its occurrence count."""
    frequencies: dict[str, int] = {}
    for word in normalize_text(text):
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies


def top_words(frequencies: dict[str, int], limit: int = 5) -> list[tuple[str, int]]:
    """Return the top N words sorted by descending count, then alphabetically."""
    ranked = sorted(
        frequencies.items(),
        key=lambda pair: (-pair[1], pair[0]),
    )
    return ranked[:limit]


def main() -> None:
    sample_paragraph = (
        "Data cleaning is essential in AI workflows. Clean data improves model "
        "accuracy, and structured data makes debugging easier. When data is messy, "
        "even a strong model struggles to generalize."
    )

    counts = count_word_frequencies(sample_paragraph)
    frequent_only = {word: count for word, count in counts.items() if count >= 2}

    print("All Word Frequencies:")
    for word, count in top_words(counts, limit=len(counts)):
        print(f"  {word:<12} -> {count}")

    print("\nWords Appearing 2+ Times (dict comprehension):")
    print(frequent_only)


if __name__ == "__main__":
    main()