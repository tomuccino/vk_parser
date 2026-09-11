import logging

from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class UrlCheckResult:
    """Результат проверки доступности одного url адреса"""
    url: str
    available: bool
    status_code: int | None = None
    error: str | None = None

    def __str__(self):
        pass

