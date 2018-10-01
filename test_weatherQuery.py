#Name: Manas
#Roll No: 2018244
#Section: B
#Group: 5

"""
This is a testing module for a1.py file.
"""

import unittest
from a1 import weather_response
from a1 import has_error
from a1 import get_temperature 
from a1 import get_humidity
from a1 import get_pressure
from a1 import get_wind
from a1 import get_sealevel


class testpoint(unittest.TestCase):

	location1 = "Delhi"
	location2 = "New York"
	location3 = "mumbai"

	apiKey = "952e9e0affed7530ec4b40516875bbe6"
	
	def test_weather_response(self):
		self.assertTrue(weather_response("Delhi",testpoint.apiKey), weather_response("delhi",testpoint.apiKey))
		self.assertTrue(weather_response(testpoint.location2,testpoint.apiKey), weather_response("new york",testpoint.apiKey))
		self.assertFalse(weather_response(testpoint.location1,testpoint.apiKey)==weather_response("Mumbai",testpoint.apiKey))
		self.assertTrue(weather_response("Delhi",testpoint.apiKey), weather_response("delhi",testpoint.apiKey))
		self.assertFalse(weather_response(testpoint.location1,testpoint.apiKey)==weather_response(testpoint.location2,testpoint.apiKey))

	def test_has_error(self):
		self.assertFalse(has_error("Delhi", weather_response("Delhi",testpoint.apiKey)))
		self.assertFalse(has_error("delhi", weather_response("Delhi",testpoint.apiKey)))
		self.assertFalse(has_error("nEw YoRk", weather_response("new york",testpoint.apiKey)))
		self.assertFalse(has_error("new york", weather_response("New york",testpoint.apiKey)))
		self.assertTrue(has_error("Delhi", weather_response("new york",testpoint.apiKey)))


	def test_get_temperature(self):
		self.assertAlmostEqual(get_temperature(weather_response(testpoint.location1, testpoint.apiKey), n=2, t="21:00:00"), 299.02, delta=15)
		self.assertAlmostEqual(get_temperature(weather_response(testpoint.location1, testpoint.apiKey), n=0, t="18:00:00"), 299.02, delta=15)
		self.assertAlmostEqual(get_temperature(weather_response(testpoint.location1, testpoint.apiKey), n=2, t="03:00:00"), 297.34, delta=15)
		self.assertAlmostEqual(get_temperature(weather_response(testpoint.location1, testpoint.apiKey), n=1, t="15:00:00"), get_temperature(weather_response("Delhi", testpoint.apiKey), n=1, t="03:00:00"), delta=15)
		self.assertAlmostEqual(get_temperature(weather_response(testpoint.location1, testpoint.apiKey), n=0, t="18:00:00"), get_temperature(weather_response("Delhi", testpoint.apiKey), n=1, t="03:00:00"), delta=15)
		self.assertIsNone(get_temperature(weather_response("Random City", testpoint.apiKey)))
		self.assertIsNone(get_temperature(weather_response("Gujarat", testpoint.apiKey), n=2))
		self.assertIsNone(get_temperature(weather_response("Baghdad", testpoint.apiKey), n=9, t="03:00:00"))
		self.assertIsNone(get_temperature(weather_response("Paris", testpoint.apiKey), n=2, t="04:03:23"))
		

	def test_get_humidity(self):
		self.assertAlmostEqual(get_humidity(weather_response(testpoint.location1, testpoint.apiKey), n=0, t="18:00:00"), 91, delta=50)
		self.assertAlmostEqual(get_humidity(weather_response(testpoint.location1, testpoint.apiKey), n=3, t="15:00:00"), 91, delta=50)
		self.assertIsNone(get_humidity(weather_response(testpoint.location1, testpoint.apiKey), n=2, t="21:00:40"))
		self.assertIsNone(get_humidity(weather_response(testpoint.location1, testpoint.apiKey), n=1, t="11:00:00"))
		self.assertAlmostEqual(get_humidity(weather_response(testpoint.location1, testpoint.apiKey), n=2, t="03:00:00"), 91, delta=50)

	def test_get_pressure(self):
		self.assertAlmostEqual(get_pressure(weather_response(testpoint.location3, testpoint.apiKey), n=1, t="00:00:00"), 1000.0, delta=50)
		self.assertAlmostEqual(get_pressure(weather_response(testpoint.location2, testpoint.apiKey), n=4, t="12:00:00"), 1000.0, delta=50)
		self.assertIsNone(get_pressure(weather_response(testpoint.location3, testpoint.apiKey), n=-2, t="15:00:00"))
		self.assertAlmostEqual(get_pressure(weather_response(testpoint.location1, testpoint.apiKey), n=1, t="18:00:00"), 1000.0, delta=50)
		self.assertIsNone(get_pressure(weather_response("Pakalu Papito", testpoint.apiKey), n=2, t="09:00:00"))
		

	def test_get_wind(self):
		self.assertAlmostEqual(get_wind(weather_response(testpoint.location1, testpoint.apiKey), n=1, t="09:00:00"), 50.0, delta=50)
		self.assertAlmostEqual(get_wind(weather_response(testpoint.location2, testpoint.apiKey), n=4, t="15:00:00"), 50.0, delta=50)
		self.assertAlmostEqual(get_wind(weather_response(testpoint.location3, testpoint.apiKey), n=2, t="18:00:00"), 50.0, delta=50)
		self.assertAlmostEqual(get_wind(weather_response(testpoint.location2, testpoint.apiKey), n=3, t="06:00:00"), 50.0, delta=50)
		self.assertAlmostEqual(get_wind(weather_response(testpoint.location3, testpoint.apiKey), n=4, t="03:00:00"), 50.0, delta=50)
		

	def test_get_sealevel(self):
		self.assertAlmostEqual(get_sealevel(weather_response(testpoint.location2, testpoint.apiKey), n=1, t="06:00:00"), 1000.0, delta=50)
		self.assertAlmostEqual(get_sealevel(weather_response(testpoint.location1, testpoint.apiKey), n=2, t="12:00:00"), 1000.0, delta=50)
		self.assertAlmostEqual(get_sealevel(weather_response(testpoint.location3, testpoint.apiKey), n=3, t="18:00:00"), 1000.0, delta=50)
		self.assertAlmostEqual(get_sealevel(weather_response(testpoint.location3, testpoint.apiKey), n=4, t="00:00:00"), 1000.0, delta=50)
		self.assertAlmostEqual(get_sealevel(weather_response(testpoint.location2, testpoint.apiKey), n=1, t="03:00:00"), 1000.0, delta=50)
		
if __name__=='__main__':
	unittest.main()
