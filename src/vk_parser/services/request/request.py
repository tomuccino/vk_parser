import requests
import logging

from dataclasses import dataclass
from utils.logger import init_logger

logger = logging.getLogger(__name__)

# from logger import init_logger


@dataclass
class Request:
    timeout: int = 5
    allow_redirects: bool = True

    def check_url_head(self, url):
        logger.debug(url)
        try:
            response = requests.head(
                url, timeout=self.timeout, allow_redirects=self.allow_redirects
            )
            return response.status_code == 200
        except requests.exceptions.RequestException as e:
            logger.exception(e)
            return False



def main():
    url = "https://my.adminvps.ru/login"

    req = Request()

    print(req.check_url_head(url))


if __name__ == "__main__":
    main()
