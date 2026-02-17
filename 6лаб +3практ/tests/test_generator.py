import unittest
from passgen.generator import generate_password


class TestGenerator(unittest.TestCase):

    def test_length(self):
        password = generate_password(10, False, False, False)
        self.assertEqual(len(password), 10)

    def test_digits(self):
        password = generate_password(20, True, False, False)
        self.assertTrue(any(c.isdigit() for c in password))

    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            generate_password(0, False, False, False)


if __name__ == "__main__":
    unittest.main()
