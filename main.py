import logging

from request import Request
from logger import init_logger

init_logger()
logger = logging.getLogger(__name__)


def main():
    url = "https://my.adminvps.ru/login"

    req = Request()

    print(req.check_url_head(url))


if __name__ == "__main__":
    main()
