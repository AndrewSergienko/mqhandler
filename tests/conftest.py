from datetime import datetime

from pytest import fixture

from mqhandler.adapters.settings import SettingsRepo
from mqhandler.domain.dto import TgMessage
from mqhandler.services.context import Context


@fixture
def tg_message() -> TgMessage:
    return TgMessage("test_username", "test_text", datetime.now())


@fixture
def context(web_session) -> Context:
    return Context(SettingsRepo(), OutputAdapter(), WebAdapter(web_session))


@fixture
def settings_repo() -> SettingsProto:
    return SettingsRepo()


@fixture
def output_adapter() -> OutputProto:
    return OutputAdapter()


@fixture
def web_adapter(web_session) -> Generator[WebProto, None, None]:
    yield WebAdapter(web_session)
    # close aiohttp session
    asyncio.run(web_session.close())


@fixture
def web_session() -> aiohttp.ClientSession:
    return get_web_session()


@fixture
def server_app() -> web.Application:
    async def handler(request: web.Request):
        return web.Response(status=200)

    app = web.Application()
    app.router.add_post("/", handler)

    return app


@fixture
def port() -> int:
    sock = socket.socket()
    sock.bind(("", 0))
    return sock.getsockname()[1]
