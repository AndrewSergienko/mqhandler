from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class TgMessage:
    username: str
    text: str
    time: datetime

    def __str__(self) -> str:
        str_time = self.time.strftime("%Y.%m.%d %H:%M")
        return f"[{str_time}] {self.username}: {self.text}"
