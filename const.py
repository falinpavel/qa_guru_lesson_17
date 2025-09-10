import os.path


class Const:

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    TESTS_DIR = os.path.join(BASE_DIR, "tests")

    SCHEMAS_DIR = os.path.join(TESTS_DIR, "schemas")
