import logging

from services.request.request import Request
from utils.logger import init_logger, dump_log, log_input, clear_dump_file
from source.urls import URLS

init_logger()
logger = logging.getLogger(__name__)


def main():
    clear_dump_file()

    request = Request()
    try:
        for url in URLS:
            print(request.check_url_head(url))
    finally:
        request.session.close()


if __name__ == "__main__":
    main()
