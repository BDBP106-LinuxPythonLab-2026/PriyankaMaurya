import re


def mask_email(match) -> str:
    email = match.group(0)
    username, domain = email.split('@')

    # Mask username if longer than 2 characters
    if len(username) > 2:
        masked_user = username[0] + '*' * (len(username) - 2) + username[-1]
    else:
        masked_user = '*' * len(username)

    return f"{masked_user}@{domain}"


def mask_text_emails(text: str) -> str:
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    # re.sub calls mask_email on every matched email address
    return re.sub(email_pattern, mask_email, text)


# Example usage
text_input = "Contact helloworld@python.com or 265hsbd026@ibab.ac.in for assistance."
masked_output = mask_text_emails(text_input)

print("Original Text:", text_input)
print("Masked Text:  ", masked_output)