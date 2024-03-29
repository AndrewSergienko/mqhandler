import asyncio
import json
import os
from dataclasses import asdict
from datetime import datetime
from pathlib import Path
from typing import Generator

import aiohttp
import fake
from pytest import fixture

from mqhandler.adapters.message import TgMessageProto, TgMessageRepo
from mqhandler.adapters.output import OutputAdapter, OutputProto
from mqhandler.adapters.settings import SettingsProto, SettingsRepo
from mqhandler.adapters.web import WebAdapter, WebProto
from mqhandler.domain.dto import TgMessage
from mqhandler.infrastructure.bootstrap import (
    get_context,
    get_root_path,
    get_web_session,
)
from mqhandler.services.context import Context


@fixture
def tg_message() -> TgMessage:
    return TgMessage("test_username", "test_text", datetime.now())


@fixture
def context(web_session) -> Context:
    return get_context(web_session, get_root_path())


@fixture
def fake_context() -> Context:
    return Context(
        fake.FakeSettingsRepo(),
        fake.FakeOutputAdapter(),
        fake.FakeWebAdapter(),
        fake.FakeTgMessageAdapter(),
        Path("fake_path"),
    )


@fixture
def settings_repo() -> SettingsProto:
    return SettingsRepo()


@fixture
def output_adapter() -> OutputProto:
    return OutputAdapter()


@fixture
def web_adapter(web_session) -> WebProto:
    return WebAdapter(web_session)


@fixture
def tg_message_repo() -> TgMessageProto:
    return TgMessageRepo()


@fixture(scope="session")
def test_file_path() -> Path:
    return get_root_path() / (os.environ.get("FILE_PATH") or "")


@fixture
def create_test_file(test_file_path, tg_message) -> None:
    with open(test_file_path, "w") as f:
        data = asdict(tg_message)
        data["time"] = tg_message.time.isoformat()
        f.write(json.dumps(data))


@fixture
def clear_test_file(test_file_path) -> Generator[None, None, None]:
    yield
    open(test_file_path, "w").close()


@fixture(scope="session", autouse=True)
def delete_test_file(test_file_path) -> Generator[None, None, None]:
    yield
    if test_file_path.exists():
        os.remove(test_file_path)


@fixture(scope="session")
def web_session() -> aiohttp.ClientSession:
    session = get_web_session()
    yield session
    asyncio.run(session.close())
