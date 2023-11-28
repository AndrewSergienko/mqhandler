import aiohttp

from mqhandler.adapters.output import OutputAdapter
from mqhandler.adapters.settings import SettingsRepo
from mqhandler.adapters.web import WebAdapter
from mqhandler.services.context import Context


def get_context(web_session: aiohttp.ClientSession) -> Context:
    return Context(SettingsRepo(), OutputAdapter(), WebAdapter(web_session))


def get_web_session() -> aiohttp.ClientSession:
    return aiohttp.ClientSession()
