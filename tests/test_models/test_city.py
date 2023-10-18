#!/usr/bin/python3
""" Defines unittest models/city.py"""
from datetime import datetime
from models.city import City
import unittest

class TestCity(unittest.TestCase):
      def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

     def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

class TestCity(TestBaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.test_class = City
        self.test_name = "City"

          def test_cityName(self):
               city = self.test_class()
        self.assertIsInstance(city.name, str)

        if __name__ == '__main__':
    unittest.main()
