import unittest

from services.request.urls_check_report import UrlsCheckReport


class TestUrlsCheckReport(unittest.TestCase):
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

    def tearDown(self):
        return super().tearDown()

    def test_init_class(self):
        url_report = UrlsCheckReport(self.urls_result)

        available = sum(r["available"] for r in self.urls_result)
        total = len(self.urls_result)
        # [print(r) for r in self.urls_result]

        self.assertEqual(url_report.total, total)
        self.assertEqual(url_report.available, available)
        self.assertEqual(url_report.unavailable, total - available)
        self.assertEqual(url_report.summary, f"Доступно {available}/{total}")


if __name__ == "__main__":
    unittest.main()
