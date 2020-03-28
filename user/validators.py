from django.core.exceptions import ValidationError
from datetime import date, datetime
import re

def validate_cc_number(value):
    if not re.match("^[0-9 ]+$", value):
        raise ValidationError("Needs to be a number.")
    if (len(value.replace(' ','')) < 13 or len(value.replace(' ', '')) > 16):
        raise ValidationError('Needs to be a credit card number.')
    else:
        return value

def validate_cc_exp(value):

    if not re.match("^(0[1-9]|10|11|12)/[0-9]{2}", value):
        raise ValidationError("Format mm/yy needed.")
    else:

        exp_year = int(value[3:])

        if exp_year < (date.today().year % 100):
            raise ValidationError("Date is expired.")


        return value

def validate_cc_security(value):

    if not re.match("^[0-9 ]+$", value):
        raise ValidationError("Needs to be a three digit number.")
    if len(value) != 3:
        raise ValidationError("Needs to be a three digit number.")
    else:
        return value

def validate_address_line(value):
    if not re.match(r"\d{1,5}\s\w{1,2}\s(\b\w*\b\s){1,2}\w*\.?", value):
        raise ValidationError("Please enter valid address.")
    else:
        return value

def validate_string(value):

    string = value.replace(' ', '')

    if not string.isalpha():
        raise  ValidationError("Invalid String.")
    else:
        return value

def validate_zip(value):

    
    if not re.match("[0-9]{5}", value):
        raise ValidationError("Enter a 5-digit zip code.")
    else:
        return value