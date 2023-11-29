import json
from dataclasses import asdict
from datetime import datetime
from pathlib import Path
from typing import Protocol

import aiofiles

from mqhandler.domain.dto import TgMessage


class TgMessageProto(Protocol):
    async def get_message(self, file_path: Path) -> TgMessage:
        """Get stored message from file."""
        pass

    async def set_message(self, file_path: Path, message: TgMessage) -> None:
        """Save message to file."""
        pass


class TgMessageRepo(TgMessageProto):
    async def get_message(self, file_path: Path) -> TgMessage:
        async with aiofiles.open(file_path, "r") as f:
            data = json.loads(await f.read())
            # convert str to datetime attr
            data["time"] = datetime.fromisoformat(data["time"])
            return TgMessage(**data)

    async def set_message(self, file_path: Path, message: TgMessage) -> None:
        async with aiofiles.open(file_path, "w") as f:
            data = asdict(message)
            # convert datetime attr to str for serialization
            data["time"] = message.time.isoformat()
            await f.write(json.dumps(data))
