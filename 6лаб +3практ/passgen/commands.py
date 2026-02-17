from .generator import generate_password
from .utils import hash_password
from .storage import load_data, save_data


def handle_generate(args) -> None:
    """
    Обрабатывает команду генерации пароля.
    """

    password = generate_password(
        args.length,
        args.digits,
        args.symbols,
        args.upper
    )

    print("Generated password:", password)

    if args.save:
        data = load_data()
        data[args.name] = hash_password(password)
        save_data(data)


def handle_list() -> None:
    """
    Выводит список сохранённых паролей.
    """

    data = load_data()

    for name in data:
        print(name)


def handle_find(args) -> None:
    """
    Ищет пароль по имени и выводит его хэш.
    """

    data = load_data()

    if args.name not in data:
        raise KeyError("Пароль не найден")

    print(data[args.name])
