import pytest
from main import is_valid_email


@pytest.mark.parametrize("email,expected", [
    ("user@gmail.com", True),
    ("user@@gmail.com", False),
    ("usergmail.com", False),
    ("user@gmail.org", True),
    ("@gmail.com", False),
    ("user@", False),
    ("", False)
])
def test_is_valid_email(email, expected):
    assert is_valid_email(email) == expected


def test_empty_email():
    assert is_valid_email("") == False


def test_email_with_no_at():
    assert is_valid_email("user.gmail.com") == False
    assert is_valid_email("gmail.com") == False
    assert is_valid_email("stevenoutlook.com") == False
