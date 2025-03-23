# def is_valid_email(email: str):
#     return "@" in email and email.endswith(".com")

def is_valid_email(email: str):
    if email.count('@') != 1:
        return False
    name, domain = email.split('@')
    if not name:
        return False
    if not (domain.startswith("gmail") or domain.startswith("outlook")):
        return False
    if not domain.endswith((".com", ".org", ".edu")):
        return False
    return True
