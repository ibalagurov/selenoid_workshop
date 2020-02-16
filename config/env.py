import os


def get(key: str, default=None) -> str:
    return os.environ.get(key=key, default=default)


def get_bool(key: str, default: bool) -> bool:
    value = get(key, default)
    return f"{value}".lower() == "true"


def get_int(key: str, default: int) -> int:
    value = get(key, default)
    return int(value)
