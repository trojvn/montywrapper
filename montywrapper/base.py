import contextlib
from pathlib import Path

from montydb import MontyClient, set_storage


class MontyBase(MontyClient):
    def __init__(self, db_path: Path):
        while True:
            with contextlib.suppress(Exception):
                set_storage(
                    str(db_path),
                    storage="sqlite",
                    use_bson=True,
                    journal_mode="WAL",
                    check_same_thread=False,
                )
                super().__init__(str(db_path))
                break
