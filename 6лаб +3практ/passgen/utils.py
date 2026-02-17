import hashlib


def hash_password(password: str) -> str:
    """
    Возвращает SHA256-хэш пароля.

    :param password: исходный пароль
    :return: строка с хэшем
    """

    return hashlib.sha256(password.encode()).hexdigest()
