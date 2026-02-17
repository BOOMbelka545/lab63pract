import unittest
import os
from passgen.storage import save_data, load_data, FILE_NAME


#python -m unittest discover tests


class TestStorage(unittest.TestCase):

    def setUp(self):
        self.test_data = {"test": "hash"}

    def tearDown(self):
        if os.path.exists(FILE_NAME):
            os.remove(FILE_NAME)

    def test_save_and_load(self):
        save_data(self.test_data)
        loaded = load_data()
        self.assertEqual(self.test_data, loaded)

    def test_load_empty(self):
        loaded = load_data()
        self.assertEqual(loaded, {})


if __name__ == "__main__":
    unittest.main()
