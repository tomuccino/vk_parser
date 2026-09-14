
import requests
import logging


logger = logging.getLogger(__name__)


class Parser:
    _st_accept: str = "text/html" 
    _st_useragent: str = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"

    def __init__(self):
        self._session = requests.Session()


    def request(self, url: str) -> str|None:
        logger.debug("Parser request %s", url)

        try:
            headers = {
                "Accept": self._st_accept,
                "User-Agent": self._st_useragent
            }

            return self._session.get(url, headers)
        except requests.exceptions.RequestException as e:
            logger.exception("Parser request %s failed", url)
            return None
        




