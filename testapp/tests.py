import requests
import unittest

URL = 'http://127.0.0.1/post_example'

A = 3
B = 2


class TestRequest(unittest.TestCase):

    def test_request_post(self):
        payload = {
            "a": A,
            "b": B
        }

        response2 = requests.post(URL, json=payload)
        self.assertEqual(int(response2.json()["resultado"]), 5)


if __name__ == '__main__':
    unittest.main()
