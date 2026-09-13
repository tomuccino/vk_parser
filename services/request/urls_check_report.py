import logging

from dataclasses import dataclass, field
from typing import Dict
from services.request.url_status import UrlStatus
from utils.logger import dump_log

logger = logging.getLogger(__name__)


@dataclass
class UrlsCheckReport:
    """Итоговый отчет об опросе всех url"""

    # urls_result: list[Dict]
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

    def result(self) -> None:
        # for url in self.urls_result:
        #     mark = "OK " if url.available else "FAIL"
        #     print(f"[{mark}] {url.url} ({url.status_code or url.error})")

        for url in self.urls_result:
            pass

        print(self.summary)
