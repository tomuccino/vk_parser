import logging

from dataclasses import dataclass
from typing import Dict
from utils.logger import dump_log

logger = logging.getLogger(__name__)

@dataclass
class UrlCheckReport:
    """Итоговый отчет об опросе всех url"""
    urls_result: list[Dict]
    total: int
    available: int
    unavailable: int
    summary: str

    def __init__(self, urls_result: list[Dict]):
        dump_log(logger, 'UrlCheckReport init', urls_result)
        self.urls_result = urls_result

    @property
    def tottal(self):
        return len(self.urls_result)

    @property
    def available(self):
        return sum(r.available for r in self.results)

    @property
    def unavailable(self):
        return self.total - self.available

    @property
    def summary(self):
        return f"Доступно {self.available}/{self.total}"

    def result(self):
        for url in self.urls_result:
            mark = "OK " if url.available else "FAIL"
            print(f"[{mark}] {url.url} ({url.status_code or url.error})")

        print(self.summary)