import logging
import pprint

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
    log_dir = CONFIG["logger"]["dir_log"]
    log_file = CONFIG["logger"]["log_file"]
    path = log_dir + log_file

    Path(path).parent.mkdir(parents=True, exist_ok=True)

    file = logging.FileHandler(path, mode="w", encoding="utf-8")
    file.setLevel(logging.DEBUG)
    file.setFormatter(
        logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(filename)s:%(lineno)d | %(funcName)s() | %(message)s",
            datefmt="%H:%M:%S",
        )
    )

    # Отдельный логгер для больших данных
    dump = logging.getLogger("dump")
    dump.propagate = False

    log_dir = CONFIG["logger"]["dir_log"]
    log_file = CONFIG["logger"]["dump_file"]
    path = log_dir + log_file
    Path(path).parent.mkdir(parents=True, exist_ok=True)

    dump.setLevel(logging.DEBUG)
    dump_file = logging.FileHandler(path, mode="w", encoding="utf-8")
    dump_file.setFormatter(logging.Formatter("%(asctime)s | %(message)s"))

    logger.addHandler(console)
    logger.addHandler(file)
    dump.addHandler(dump_file)


def dump_log(logger, label, data, max_lines=20):
    """Красивый вывод структур с ограничением"""

    text = pprint.pformat(data, width=120, compact=True)
    lines = text.split("\n")

    if len(lines) > max_lines:
        lines = lines[:max_lines] + [f"... ещё {len(lines) - max_lines} строк"]

    # logger.debug(f"{label}:\n" + "\n".join(lines))

    log_dir = CONFIG["logger"]["dir_log"]
    log_file = CONFIG["logger"]["dump_file"]
    path = log_dir + log_file
    with open(path, "a") as file:
        file.write("\n".join(lines))


def log_input(logger, label, data):
    """Логирует метаданные о данных вместо самих данных"""
    if isinstance(data, (list, tuple, set)):
        type_name = type(data).__name__
        first_type = type(data[0]).__name__ if data else "empty"
        logger.debug(f"{label}: {type_name}[{len(data)}] of {first_type}")

    elif isinstance(data, dict):
        keys = list(data.keys())[:5]
        logger.debug(f"{label}: dict({len(data)}) keys={keys}")

    elif isinstance(data, str):
        preview = data[:50].replace("\n", "\\n")
        logger.debug(f"{label}: str({len(data)}) {preview!r}")

    elif isinstance(data, bytes):
        logger.debug(f"{label}: bytes({len(data)})")

    else:
        logger.debug(f"{label}: {type(data).__name__} = {repr(data)[:100]}")


def clear_dump_file():
    """Создает пустой файл или перезаписывает существующий."""
    log_dir = CONFIG["logger"]["dir_log"]
    log_file = CONFIG["logger"]["dump_file"]
    path = log_dir + log_file

    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        pass  # Просто создаем пустой файл
