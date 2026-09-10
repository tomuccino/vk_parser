import logging

from request import Request
from logger import init_logger, dump_log, log_input, clear_dump_file

init_logger()
logger = logging.getLogger(__name__)


def main():
    clear_dump_file()

    url = "https://my.adminvps.ru/login"
    req = Request()
    print(req.check_url_head(url))

    data = {
        f"user_{i:02d}": {
            "id": i,
            "name": f"User_{i}",
            "age": 20 + (i % 40),
            "email": f"user{i}@example.com",
            "city": ["Москва", "СПб", "Казань", "Сочи", "Омск"][i % 5],
            "active": i % 2 == 0,
            "score": round(10 + i * 1.5, 2),
            "tags": [f"tag_{i}", f"group_{i % 3}"],
        }
        for i in range(1, 31)
    }

    dump_log(logger, 'test', data)
    log_input(logger,'test', data)





if __name__ == "__main__":
    main()
