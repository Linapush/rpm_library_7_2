from django.forms import ChoiceField, Form
from .config import LOCATIONS_NAMES

class WeatherForm(Form):
    location = ChoiceField(label='location', choices=LOCATIONS_NAMES)
