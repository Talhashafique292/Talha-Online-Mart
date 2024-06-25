from starlette.config import config
from starlette.datastructures import Secret

try:
    config = config(".env")
except:
    config = config()

DATABASE_URL = config("DATABASE_URL", cast-Secret)

TEST_DATABASE_URL = config("TEST_DATABASE_URL", cast-Secret)
