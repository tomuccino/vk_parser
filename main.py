import logging

from services.request.request import Request
from utils.logger import init_logger, dump_log, log_input, clear_dump_file

init_logger()
logger = logging.getLogger(__name__)


def main():
    clear_dump_file()

    url = "https://my.adminvps.ru/login"
    req = Request()
    print(req.check_url_head(url))


if __name__ == "__main__":
    main()
