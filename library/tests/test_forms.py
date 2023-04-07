from django.test import TestCase
from library_app.forms import WeatherForm
from library_app.config import LOCATIONS_COORDINATES
from random import sample
from string import ascii_lowercase

class WeatherFormTests(TestCase):

    def test_appropriate(self):
        if LOCATIONS_COORDINATES:
            WeatherForm(data={'location': list(LOCATIONS_COORDINATES.keys())[0]})
        else:
            raise Exception('Locations for weather page are not provided')

    def test_failing(self):
        if LOCATIONS_COORDINATES:
            location = ''.join(sample(ascii_lowercase, 10))
            while location in LOCATIONS_COORDINATES.keys():
                location = ''.join(sample(ascii_lowercase, 10))
            form = WeatherForm(data={'location': location})
            error = f'Выберите корректный вариант. {location} нет среди допустимых значений.'
            self.assertEqual(form.errors['location'], [error])
        else:
            raise Exception('Locations for weather page are not provided')
