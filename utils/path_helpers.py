import os
from pathlib import Path


def get_schema_path(schema_name):
    base_directory = Path(__file__).resolve().parent.parent
    return os.path.join(base_directory, 'tests', 'schemas', schema_name)
