# Input helpers — keep menus simple and prevent crashes on bad input
from datetime import datetime


def ask_text(prompt, field_name="This field"):
    """Require non-empty text."""
    while True:
        value = input(prompt).strip()
        if not value:
            print(f"{field_name} cannot be empty. Please try again.")
            continue
        return value


def ask_name(prompt="Name: "):
    """Client name: non-empty, must contain at least one letter."""
    while True:
        value = input(prompt).strip()
        if not value:
            print("Name cannot be empty. Please try again.")
            continue
        if not any(ch.isalpha() for ch in value):
            print("Name must contain letters, not only numbers or symbols.")
            continue
        return value


def ask_phone(prompt="Phone: "):
    """
    Phone must be exactly 10 digits and start with 0.
    Rejects letters, symbols, spaces, negatives, decimals, wrong length.
    Example valid: 0772456372
    """
    while True:
        value = input(prompt).strip()
        if not value:
            print("Phone number cannot be empty.")
            continue
        if not value.isdigit():
            print("Phone number must contain digits only (no letters, spaces or symbols).")
            continue
        if len(value) != 10:
            print("Phone number must be exactly 10 digits (e.g. 0772456372).")
            continue
        if not value.startswith("0"):
            print("Phone number must start with 0 (e.g. 0772456372).")
            continue
        return value


def ask_email(prompt="Email: "):
    """Simple required email check: non-empty and contains '@'."""
    while True:
        value = input(prompt).strip()
        if not value:
            print("Email cannot be empty.")
            continue
        if "@" not in value or value.startswith("@") or value.endswith("@"):
            print("Enter a valid email address (must contain @).")
            continue
        return value


def ask_positive_float(prompt, field_name="Value"):
    """Require a number greater than zero. Rejects text, negatives, zero."""
    while True:
        raw = input(prompt).strip()
        if not raw:
            print(f"{field_name} cannot be empty.")
            continue
        try:
            number = float(raw)
        except ValueError:
            print(f"{field_name} must be a number (not text). Please try again.")
            continue
        if number <= 0:
            print(f"{field_name} must be greater than zero. Please try again.")
            continue
        return number


def ask_positive_int(prompt, field_name="Number", minimum=1, maximum=None):
    """Require a whole number in an optional range. Rejects text, decimals, negatives."""
    while True:
        raw = input(prompt).strip()
        if not raw:
            print(f"{field_name} cannot be empty.")
            continue
        if "." in raw:
            print(f"{field_name} must be a whole number (no decimals).")
            continue
        try:
            number = int(raw)
        except ValueError:
            print(f"{field_name} must be a whole number (not text). Please try again.")
            continue
        if number < minimum:
            print(f"{field_name} must be at least {minimum}. Please try again.")
            continue
        if maximum is not None and number > maximum:
            print(f"{field_name} must be at most {maximum}. Please try again.")
            continue
        return number


def ask_date(prompt, field_name="Date"):
    """
    Accept only YYYY-MM-DD and a real calendar date.
    Returns the validated string (same format the rest of the program uses).
    """
    while True:
        raw = input(prompt).strip()
        if not raw:
            print(f"{field_name} cannot be empty.")
            continue
        try:
            datetime.strptime(raw, "%Y-%m-%d")
        except ValueError:
            print(f"{field_name} must be a valid date in YYYY-MM-DD format "
                  f"(e.g. 2025-01-15). Please try again.")
            continue
        return raw


def ask_policy_dates():
    """Ask start and end dates; end must be strictly after start."""
    while True:
        start = ask_date("Start date (YYYY-MM-DD): ", "Start date")
        end = ask_date("End date (YYYY-MM-DD): ", "End date")
        start_d = datetime.strptime(start, "%Y-%m-%d").date()
        end_d = datetime.strptime(end, "%Y-%m-%d").date()
        if end_d <= start_d:
            print("End date must be after start date. Please enter both dates again.")
            continue
        return start, end


def ask_claim_date(policy):
    """
    Claim date must be a valid YYYY-MM-DD date.
    Optionally warn if outside the policy period.
    """
    while True:
        claim_date = ask_date("Date (YYYY-MM-DD): ", "Claim date")
        try:
            c = datetime.strptime(claim_date, "%Y-%m-%d").date()
            start = datetime.strptime(policy._start_date, "%Y-%m-%d").date()
            end = datetime.strptime(policy._end_date, "%Y-%m-%d").date()
        except (ValueError, AttributeError):
            return claim_date
        if c < start or c > end:
            print(f"Claim date should fall within the policy period "
                  f"({policy._start_date} to {policy._end_date}).")
            retry = input("Use this date anyway? (y/n): ").strip().lower()
            if retry == "y":
                return claim_date
            continue
        return claim_date
