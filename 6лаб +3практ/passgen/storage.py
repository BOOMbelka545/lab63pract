import json
import os

FILE_NAME = "passwords.json"


def load_data() -> dict:
    """
    Загружает данные из JSON-файла.

    :return: словарь с сохранёнными паролями
    """

    try:
        if not os.path.exists(FILE_NAME):
            return {}

        with open(FILE_NAME, "r", encoding="utf-8") as f:
            return json.load(f)

    except json.JSONDecodeError:
        return {}
    except OSError:
        return {}


def save_data(data: dict) -> None:
    """
    Сохраняет данные в JSON-файл.

    :param data: словарь для сохранения
    """

    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
