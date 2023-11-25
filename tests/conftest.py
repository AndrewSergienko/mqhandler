from datetime import datetime

from pytest import fixture

from mqhandler.domain.dto import TgMessage


@fixture
def tg_message() -> TgMessage:
    return TgMessage("test_username", "test_text", datetime.now())
