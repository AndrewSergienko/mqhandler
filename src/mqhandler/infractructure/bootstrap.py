import logging
from pathlib import Path

import aiohttp

from mqhandler.adapters.message import TgMessageRepo
from mqhandler.adapters.output import OutputAdapter
from mqhandler.adapters.settings import SettingsRepo
from mqhandler.adapters.web import WebAdapter
from mqhandler.services.context import Context


def get_context(
    web_session: aiohttp.ClientSession, root_path: Path
) -> Context:
    return Context(
        SettingsRepo(),
        OutputAdapter(),
        WebAdapter(web_session),
        TgMessageRepo(),
        root_path,
    )


def get_web_session() -> aiohttp.ClientSession:
    return aiohttp.ClientSession()


def logging_setup() -> None:
    FORMAT = "[%(filename)s:%(lineno)s - %(funcName)20s()] %(message)s"
    logging.basicConfig(format=FORMAT)


def get_root_path() -> Path:
    return Path(__file__).parent.parent.parent.parent


async def get_mq_url(context: Context) -> str:
    address = await context.settings.get("AMQP_ADDRESS", raise_exc=True)
    port = await context.settings.get("AMQP_PORT", raise_exc=True)
    user = await context.settings.get("AMQP_USER", raise_exc=True)
    password = await context.settings.get("AMQP_PASSWORD", raise_exc=True)
    return f"ampq://{user}:{password}@{address}:{port}/"
