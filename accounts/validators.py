from django.core.exceptions import ValidationError
import re


def validate_phone(value):

    pattern = r"^09\d{9}$"

    if not re.match(pattern, value):
        raise ValidationError("Phone number is not valid.")