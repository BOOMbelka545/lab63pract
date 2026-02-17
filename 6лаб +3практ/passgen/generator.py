import secrets
import string


def generate_password(length: int, digits: bool, symbols: bool, upper: bool) -> str:
    """
    Генерирует случайный пароль заданной длины.

    :param length: длина пароля
    :param digits: использовать ли цифры
    :param symbols: использовать ли специальные символы
    :param upper: использовать ли заглавные буквы
    :return: сгенерированный пароль

    :raises ValueError: если длина <= 0
    """

    if length <= 0:
        raise ValueError("Длина пароля должна быть положительной")

    chars = string.ascii_lowercase

    if upper:
        chars += string.ascii_uppercase
    if digits:
        chars += string.digits
    if symbols:
        chars += string.punctuation

    return "".join(secrets.choice(chars) for _ in range(length))
