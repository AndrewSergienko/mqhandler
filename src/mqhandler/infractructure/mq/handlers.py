from typing import Any, Callable, Coroutine

import aio_pika.abc
from aio_pika.abc import AbstractIncomingMessage

from mqhandler.services.context import Context

handlers_type_hint = dict[
    str, Callable[[AbstractIncomingMessage], Coroutine[Any, Any, None]]
]


def get_handlers(context: Context) -> handlers_type_hint:
    async def command_handler(
        message: aio_pika.abc.AbstractIncomingMessage,
    ) -> None:
        async with message.process():
            print(message.body)

    async def bot_message_handler(
        message: aio_pika.abc.AbstractIncomingMessage,
    ) -> None:
        async with message.process():
            print(message.body)

    return {"commands": command_handler, "bot": bot_message_handler}
