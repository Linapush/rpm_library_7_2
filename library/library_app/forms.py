from django.forms import ChoiceField, Form, DecimalField
from .config import LOCATIONS_NAMES, DECIMAL_MAX_DIGITS, DECIMAL_PLACES


class WeatherForm(Form):
    location = ChoiceField(label='location', choices=LOCATIONS_NAMES)


class AddFundsForm(Form):
    money = DecimalField(
        label='Amount',
        max_digits=DECIMAL_MAX_DIGITS,
        decimal_places=DECIMAL_PLACES,
    )
