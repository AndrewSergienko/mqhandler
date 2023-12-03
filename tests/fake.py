from datetime import datetime
from pathlib import Path

from mqhandler.adapters.message import TgMessageProto
from mqhandler.adapters.output import OutputProto
from mqhandler.adapters.settings import SettingsProto
from mqhandler.adapters.web import WebProto
from mqhandler.domain.dto import TgMessage


class FakeTgMessageAdapter(TgMessageProto):
    def __init__(self):
        self.message = TgMessage(
            username="test", text="test", time=datetime.now()
        )

    async def get_message(self, file_path: Path) -> TgMessage:
        return self.message

    async def set_message(self, file_path: Path, message: TgMessage) -> None:
        self.message = message


class FakeOutputAdapter(OutputProto):
    def __init__(self):
        self.result = None

    async def info(self, msg: str) -> None:
        self.result = msg


class FakeSettingsRepo(SettingsProto):
    async def get(self, name: str, raise_exc=False) -> str | None:
        data = {"EXTERNAL_API_URL": "test_url", "FILE_PATH": "test_path"}
        return data.get(name)


class FakeWebAdapter(WebProto):
    def __init__(self):
        self.result = None

    async def post(self, url: str, data: dict) -> int:
        self.result = {"url": url, "data": data}
        return 200
