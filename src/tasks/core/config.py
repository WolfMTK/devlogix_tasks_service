import os

from dataclasses import dataclass


@dataclass
class Settings:
    db_url: str = os.getenv(
        'DB_URL',
        'sqlite+aiosqlite:///db.db'
    )
