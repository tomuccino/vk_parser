import logging

from bs4 import BeautifulSoup
from utils.logger import dump_log


logger = logging.getLogger(__name__)

class DataParser:
    def __init__(self, response: str):
        dump_log(logger, 'DataParser init', response)

        self._response = response

    @property
    def _parse_response_bs(self):
        return BeautifulSoup(self._response.text,"lxml")

    def get_data(self):
        dump_log(logger, 'DataParser response_bs', self._parse_response_bs)
        logger.info("parse data from ")
        bs = self._parse_response_bs

        print(bs)