#!/usr/bin/python3
"""Defines unittests for models/amenity.py"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime
import time
from models.engine.file_storage import FileStorage
from models import storage

class TestAmenity(unittest.TestCase):
    """Amenity model class test case"""

  def setUp(self):
        """Sets up test methods."""
        pass

 def tearDown(self):
     def tearDownClass(class):
         
        """Destroy JSON file"""
        del class.amenity
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

class TestFileStorage(unittest.TestCase):

    """FileStorage test"""
    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        self.test_class = FileStorage

   def test_is_subclass(self):
        self.assertTrue(issubclass(self.amenity.__class__, BaseModel))

    def checking_for_doc(self):
        self.assertIsNotNone(Amenity.__doc__)

class TestFileStorage(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        self.test_class = FileStorage

        class TestAmenity(TestBaseModel):
            def __init__(self, *args, **kwargs):
                 super().__init__(*args, **kwargs)
        self.test_class = Amenity
        self.test_name = "Amenity"

         def test_amenity(self):
             amenity = self.test_class()
        self.assertIsInstance(amenity.name, str)

if __name__ == "__main__":
    unittest.main()
