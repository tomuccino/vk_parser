import logging

from services.request.request import Request
from services.request.urls_check_report import UrlsCheckReport
from services.parser.parser import Parser
from services.parser.data_parser import DataParser
from utils.logger import init_logger, clear_dump_file
from source.urls import URLS

init_logger()
logger = logging.getLogger(__name__)


def check_urls(request: Request, report: UrlsCheckReport) -> None:
    """Проверка доступности URL."""
    try:
        for url in URLS:
            checked_url = request.check_url_head(url)
            # report.append(checked_url)
            report.urls_result.append(checked_url)
    finally:
        request.session.close()

    print(report.full_report)


def parse_urls(parser: Parser) -> None:
    """Парсинг данных со страниц."""
    for url in URLS:
        try:
            data = parser.request(url)
            data_parser = DataParser(data)
            data_parser.get_data()
        except Exception as e:
            logger.exception(f"Ошибка при парсинге {url}: {e}")


def main():
    clear_dump_file()

    request = Request()
    urls_report = UrlsCheckReport()

    check_urls(request, urls_report)

    parser = Parser()
    parse_urls(parser)


if __name__ == "__main__":
    main()
