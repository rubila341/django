import json
import os
import unittest


def write_to_file(file_name, data):
    try:
        with open(file_name, 'w') as f:
            json.dump(data, f)
    except TypeError as err:
        raise err
    except IOError as err:
        raise err


def read_from_file(file_name):
    try:
        with open(file_name, 'r') as f:
            return json.load(f)
    except FileNotFoundError as err:
        raise err
    except IOError as err:
        raise err


class TestFileOperations(unittest.TestCase):

    def setUp(self):
        self.file_name = "test.json"
        self.test_data = {
            "pk": 4,
            "title": "Test Title",
            "author": "Test Author",
            "published_date": "2024-06-23",
            "publisher": 6,
            "price": 9.99,
            "discounted_price": 3.56,
            "is_bestseller": True,
            "is_banned": False,
            "genres": ["fiction", "drama"]
        }

    def tearDown(self):
        if os.path.exists(self.file_name):
            os.remove(self.file_name)

    def test_write_and_read_file(self):
        write_to_file(self.file_name, self.test_data)
        data = read_from_file(self.file_name)
        self.assertEqual(data["pk"], 4)
        self.assertEqual(data["title"], "Test Title")
        self.assertEqual(data["price"], 9.99)
        self.assertTrue(data["is_bestseller"])

    def test_write_and_read_empty_file(self):
        empty_data = {}
        write_to_file(self.file_name, empty_data)
        data = read_from_file(self.file_name)
        self.assertEqual(data, {})

    def test_read_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            read_from_file("nonexistent.json")

    def test_write_bad_data_into_file(self):
        bad_data = set([1, 2, 3])
        with self.assertRaises(TypeError):
            write_to_file(self.file_name, bad_data)


if __name__ == '__main__':
    unittest.main()
