import unittest
import requests

class TestWeatherAPIIntegration(unittest.TestCase):

    BASE_URL = 'http://wttr.in'

    def test_get_weather_for_city(self):
        response = requests.get(f'{self.BASE_URL}/London?format=j1')
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('current_condition', data)

    def test_get_weather_invalid_city(self):
        response = requests.get(f'{self.BASE_URL}/InvalidCity')
        self.assertEqual(response.status_code, 404)

    def test_get_weather_format_json(self):
        response = requests.get(f'{self.BASE_URL}/Moscow?format=j1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'application/json')

    def test_get_weather_multiple_cities(self):
        cities = ["London", "New+York"]
        responses = [requests.get(f'{self.BASE_URL}/{city}?format=j1') for city in cities]
        for response in responses:
            self.assertEqual(response.status_code, 200)

    def test_get_current_time_for_city(self):
        response = requests.get(f'{self.BASE_URL}/London?format=j1')
        self.assertEqual(response.status_code, 200)
        data = response.json()

        self.assertIn('current_condition', data)
        self.assertIn('observation_time', data['current_condition'][0])


if __name__ == '__main__':
    unittest.main()


