import os
from pathlib import Path


def get_schema_path(schema_name):
    """Возвращает абсолютный путь к файлу схемы"""
    base_directory = Path(__file__).resolve().parent.parent
    return os.path.join(base_directory, 'tests', 'schemas', schema_name)
