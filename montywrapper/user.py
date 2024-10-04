import contextlib
from pathlib import Path

from montydb import MontyCollection, MontyDatabase

from .base import MontyBase


class MontyUser(MontyBase):
    def __init__(self, db_path: Path, collection: str):
        self.__db_path = db_path
        self.__collection = collection
        super().__init__(db_path)

    @property
    def db(self) -> MontyDatabase:
        return self[self.__db_path.name]

    @property
    def collection(self) -> MontyCollection:
        return self.db[self.__collection]

    def check_auth(self) -> bool:
        """Проверка авторизации"""
        with contextlib.suppress(Exception):
            self.collection.find_one({"_id": 1})
            return True
        return False
