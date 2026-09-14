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

        available_urls = [url for url in report.urls_result if url.status_code == 200]

        print(available_urls)

    finally:
        request.session.close()

    # return ???
    print(report.full_report)
    print(available_urls)



def parse_urls(parser: Parser) -> None:
    """Парсинг данных со страниц."""
        # data = parser.request(url)
        # data_parser = DataParser(data)
        # data_parser.get_data()
        # logger.exception(f"Ошибка при парсинге {url}: {e}")


def main():
    clear_dump_file()

    request = Request()
    urls_report = UrlsCheckReport()

    check_urls(request, urls_report)

    parser = Parser()
    # parse_urls(parser)


if __name__ == "__main__":
    main()
