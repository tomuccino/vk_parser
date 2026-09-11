import logging

from dataclasses import dataclass
from tkinter import NO
from typing import Dict
from utils.logger import dump_log

logger = logging.getLogger(__name__)


@dataclass
class UrlsCheckReport:
    """Итоговый отчет об опросе всех url"""

    urls_result: list[Dict]
    # total: int
    # available: int
    # unavailable: int
    # summary: str

    def __init__(self, urls_result: list[Dict]):
        dump_log(logger, "UrlCheckReport init", urls_result)
        self.urls_result = urls_result

    @property
    def total(self) -> int:
        return len(self.urls_result)

    @property
    def available(self) -> int:
        return sum(r["available"] for r in self.urls_result)

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
            print()

        print(self.summary)
