import re


def get_unique_emails(text: str) -> list[str]:
    # Regex pattern to match standard email structures
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    # re.findall returns all occurrences; set() keeps only unique ones
    unique_emails = set(re.findall(email_pattern, text))
    return sorted(list(unique_emails))


# Example usage
sample_text = """
Reach out to 265hsbd026@ibab.ac.in or support@ibab.ac.in.
For secondary contact, use 265hsbd026@ibab.ac.in or info@domain.org.
"""

emails = get_unique_emails(sample_text)
print("Unique emails found:", emails)