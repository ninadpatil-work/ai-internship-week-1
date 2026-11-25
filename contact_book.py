def normalize_key(name: str) -> str:
    """Normalize contact names for consistent dictionary keys."""
    return " ".join(name.strip().lower().split())


def add_contact(
    book: dict[str, dict[str, object]],
    name: str,
    phone: str,
    email: str = "",
    tags: list[str] | None = None,
) -> bool:
    """Add a new contact. Returns False if a contact with that name already exists."""
    key = normalize_key(name)
    if not key or key in book:
        return False

    cleaned_tags = [t.strip().lower() for t in (tags or []) if t.strip()]
    book[key] = {
        "display_name": " ".join(name.strip().split()).title(),
        "phone": phone.strip(),
        "email": email.strip().lower(),
        "tags": cleaned_tags,
    }
    return True


def get_contact(book: dict[str, dict[str, object]], name: str) -> dict[str, object] | None:
    """Retrieve a contact record by name, or None if not found."""
    return book.get(normalize_key(name))


def update_contact(
    book: dict[str, dict[str, object]],
    name: str,
    phone: str | None = None,
    email: str | None = None,
    new_tags: list[str] | None = None,
) -> bool:
    """Update fields on an existing contact. Returns False if the contact does not exist."""
    record = get_contact(book, name)
    if record is None:
        return False

    if phone is not None and phone.strip():
        record["phone"] = phone.strip()
    if email is not None:
        record["email"] = email.strip().lower()
    if new_tags is not None:
        record["tags"] = [t.strip().lower() for t in new_tags if t.strip()]
    return True


def delete_contact(book: dict[str, dict[str, object]], name: str) -> bool:
    """Delete a contact by name. Returns True if removed, False if absent."""
    return book.pop(normalize_key(name), None) is not None


def search_by_tag(book: dict[str, dict[str, object]], tag: str) -> dict[str, dict[str, object]]:
    """Return a filtered dictionary of contacts matching a given tag."""
    target = tag.strip().lower()
    return {
        key: info
        for key, info in book.items()
        if target in info.get("tags", [])
    }


def format_contact(info: dict[str, object]) -> str:
    """Format a single contact dictionary for readable display."""
    tags_list = info.get("tags", [])
    tags_display = ", ".join(tags_list) if tags_list else "none"
    email_display = info.get("email") or "N/A"
    return (
        f"{info['display_name']} | Phone: {info['phone']} | "
        f"Email: {email_display} | Tags: [{tags_display}]"
    )


def main() -> None:
    contacts: dict[str, dict[str, object]] = {}

    add_contact(
        contacts,
        name="Aarav Kulkarni",
        phone="+91-98201-11223",
        email="aarav.k@example.com",
        tags=["mentor", "python"],
    )
    add_contact(
        contacts,
        name="Meera Deshmukh",
        phone="+91-98700-44556",
        email="meera.d@example.com",
        tags=["study-group", "ai"],
    )
    add_contact(
        contacts,
        name="Rohan Joshi",
        phone="+91-98111-22334",
        tags=["python", "ai"],
    )

    # Update an existing contact
    update_contact(contacts, "rohan joshi", email="rohan.joshi@example.com")

    print("--- All Contacts ---")
    for info in contacts.values():
        print(format_contact(info))

    print("\n--- Contacts Tagged 'python' ---")
    python_contacts = search_by_tag(contacts, "python")
    for info in python_contacts.values():
        print(format_contact(info))

    # Delete a contact safely
    deleted = delete_contact(contacts, "Meera Deshmukh")
    print(f"\nDeleted 'Meera Deshmukh': {deleted} | Remaining count: {len(contacts)}")


if __name__ == "__main__":
    main()