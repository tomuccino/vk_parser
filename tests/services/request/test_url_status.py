import unittest

from services.request.url_status import UrlStatus


class TestUrlStatus(unittest.TestCase):
    def setUp(self):
        # return super().setUp()
        self.urls_result = [
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

    def test_init_class(self):
        for url in self.urls_result:
            url_result = UrlStatus(**url)

            mark = " OK " if url["available"] else "FAIL"
            result_str = (
                f"[ {mark} ] {url['url']} ({url['status_code'] or url['error']})"
            )
            self.assertEqual(str(url_result), result_str)
