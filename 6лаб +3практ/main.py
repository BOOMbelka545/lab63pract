"""
Главный файл приложения.

Точка входа в программу.
Обрабатывает аргументы командной строки с помощью argparse
и передаёт управление соответствующим обработчикам команд.
"""

# python main.py generate --length 12 --digits --symbols --upper
# python main.py generate --save --name gmail
# cat passwords.json
# python main.py list
# python main.py find --name gmail
# python -m unittest

import argparse

from passgen.commands import (
    handle_generate,
    handle_list,
    handle_find
)


def main() -> None:
    """
    Настраивает CLI-интерфейс и запускает обработку команд.
    """

    parser = argparse.ArgumentParser(
        description="CLI-генератор безопасных паролей"
    )

    subparsers = parser.add_subparsers(dest="command")

    # ---------- generate ----------
    gen_parser = subparsers.add_parser(
        "generate",
        help="Сгенерировать новый пароль"
    )

    gen_parser.add_argument("--length", type=int, default=12,
                            help="Длина пароля")

    gen_parser.add_argument("--digits", action="store_true",
                            help="Добавить цифры")

    gen_parser.add_argument("--symbols", action="store_true",
                            help="Добавить спецсимволы")

    gen_parser.add_argument("--upper", action="store_true",
                            help="Добавить заглавные буквы")

    gen_parser.add_argument("--save", action="store_true",
                            help="Сохранить пароль в файл")

    gen_parser.add_argument("--name", type=str, default="default",
                            help="Имя для сохранения")

    # ---------- list ----------
    subparsers.add_parser(
        "list",
        help="Показать список сохранённых паролей"
    )

    # ---------- find ----------
    find_parser = subparsers.add_parser(
        "find",
        help="Найти пароль по имени"
    )

    find_parser.add_argument("--name", required=True,
                             help="Имя сохранённого пароля")

    args = parser.parse_args()

    try:
        if args.command == "generate":
            handle_generate(args)

        elif args.command == "list":
            handle_list()

        elif args.command == "find":
            handle_find(args)

        else:
            parser.print_help()

    except Exception as e:
        print("Ошибка:", e)


if __name__ == "__main__":
    main()
