import logging

from dataclasses import dataclass, field
from typing import Dict
from services.request.url_status import UrlStatus
from utils.logger import dump_log

logger = logging.getLogger(__name__)


@dataclass
class UrlsCheckReport:
    """Итоговый отчет об опросе всех url

        Attributes:

            urls_result: list = [
                {
                    url: str
                    available: bool
                    status_code: int | None = None
                    error: str | None = None
                },
            ]
            full_report: str
    """

    urls_result: list[UrlStatus] = field(default_factory=list)

    # total: int
    # available: int
    # unavailable: int
    # summary: str

    def __post_init__(self):
        dump_log(logger, "UrlCheckReport init", self.urls_result)

    @property
    def total(self) -> int:
        return len(self.urls_result)

    @property
    def available(self) -> int:
        return sum(r.available for r in self.urls_result)

    @property
    def unavailable(self) -> int:
        return self.total - self.available

    @property
    def summary(self) -> str:
        return f"Доступно {self.available}/{self.total}"

    @property
    def result(self) -> str:
        return "\n".join(str(url) for url in self.urls_result)

    @property
    def full_report(self) -> str:
        return (
            "=== Полный отчет о проверке адресов ===\n"
            "\n"
            f"{self.result}\n"
            f"{self.summary}"
        )

