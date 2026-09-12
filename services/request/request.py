import requests
import logging

from dataclasses import dataclass
from services.request.url_status import UrlStatus

logger = logging.getLogger(__name__)

# from logger import init_logger


@dataclass
class Request:
    timeout: int = 5
    allow_redirects: bool = True

    def check_url_head(self, url) -> UrlStatus:
        logger.debug(url)
        try:
            response = requests.head(
                url, timeout=self.timeout, allow_redirects=self.allow_redirects
            )
            # return response.status_code == 200
            logger.info(
                "check url: %s -> %s (final url: %s)",
                url,
                response.status_code,
                response.url,
            )
            return UrlStatus(
                url=url,
                available=response.status_code == 200,
                status_code=response.status_code,
            )
        except requests.exceptions.RequestException as e:
            logger.exception(e)
            return UrlStatus(url=url, available=False, status_code=None, error=str(e))


def main():
    url = "https://my.adminvps.ru/login"

    req = Request()

    print(req.check_url_head(url))


if __name__ == "__main__":
    main()
