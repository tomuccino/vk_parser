import unittest

class TestRequest(unittest.TestCase):
    def setUp(self):
        # return super().setUp()
        self.urls_result = items = [
        {
            "url": "https://example.com",
            "available": True,
            "status_code": 200,
            "error": None,
        },
        {
            "url": "https://example.org",
            "available": False,
            "status_code": 404,
            "error": "Not Found",
        },
        {
            "url": "https://example.net",
            "available": False,
            "status_code": None,
            "error": "Connection timeout",
        },
        ]

    def tearDown(self):
        return super().tearDown()

    