from city_functions import city_country
import unittest

class CityCountryTestCase(unittest.TestCase):
    def test_first_city_country_name(self):
        cityCountry = city_country('santiago','chile')
        self.assertEqual(cityCountry,'Santiago, Chile')

unittest.main()