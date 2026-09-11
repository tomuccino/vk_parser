import logging

from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class UrlStatus:
    """Результат проверки доступности одного url адреса"""

    url: str
    available: bool
    status_code: int | None = None
    error: str | None = None

    def __str__(self):
        mark = " OK " if self.available else "FAIL"
        return f"[ {mark} ] {self.url} ({self.status_code or self.error})"
