import pytest

from mqhandler.adapters.message import TgMessageProto
from mqhandler.adapters.output import OutputProto
from mqhandler.adapters.settings import SettingsProto
from mqhandler.adapters.web import WebProto
from mqhandler.services.context import Context


class TestContext:
    @pytest.mark.asyncio
    async def test_context(self, context: Context) -> None:
        assert issubclass(type(context.message), TgMessageProto)
        assert issubclass(type(context.web), WebProto)
        assert issubclass(type(context.output), OutputProto)
        assert issubclass(type(context.settings), SettingsProto)
