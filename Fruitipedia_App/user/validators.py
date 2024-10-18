from django.core.exceptions import ValidationError
import re


def validate_name(value):
    if not re.match(r'^[A-Za-z]', value):
        raise ValidationError("Your name must start with a letter!")
