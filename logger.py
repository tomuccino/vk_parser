import logging

from pathlib import Path
from config import CONFIG


def init_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Консоль: только INFO и выше
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(
        logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(message)s", datefmt="%H:%M:%S"
        )
    )

    # Файл: DEBUG и выше (всё)
    log_path = CONFIG["logger"]["log_file_path"]
    Path(log_path).parent.mkdir(parents=True, exist_ok=True)

    file = logging.FileHandler(log_path, mode="w", encoding="utf-8")
    file.setLevel(logging.DEBUG)
    file.setFormatter(
        logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(filename)s:%(lineno)d | %(funcName)s() | %(message)s",
            datefmt="%H:%M:%S",
        )
    )

    logger.addHandler(console)
    logger.addHandler(file)
