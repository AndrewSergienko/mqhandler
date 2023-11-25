from datetime import datetime

from pytest import fixture

from mqhandler.adapters.settings import SettingsRepo
from mqhandler.domain.dto import TgMessage
from mqhandler.services.context import Context


@fixture
def tg_message() -> TgMessage:
    return TgMessage("test_username", "test_text", datetime.now())


@fixture
def context() -> Context:
    return Context(SettingsRepo())
