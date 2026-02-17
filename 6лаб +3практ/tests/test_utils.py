import unittest
from passgen.utils import hash_password


class TestUtils(unittest.TestCase):

    def test_hash(self):
        h1 = hash_password("123")
        h2 = hash_password("123")

        self.assertEqual(h1, h2)
        self.assertNotEqual(h1, "123")


if __name__ == "__main__":
    unittest.main()
