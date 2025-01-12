from enum import Enum


class AllowedDBMS(str, Enum):
    mysql = "mysql"
    postgresql = "postgresql"
    sqlite = "sqlite"
