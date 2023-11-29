import json
import logging
from typing import Any, Callable, Coroutine

import aio_pika.abc
from adaptix import Retort

from mqhandler.domain.dto import TgMessage
from mqhandler.services import message as services
from mqhandler.services.context import Context

# type hints
Message = aio_pika.abc.AbstractIncomingMessage
Handler = Callable[[Message], Coroutine[Any, Any, None]]


def get_handlers(context: Context) -> dict[str, Handler]:
    """
    Initialize and return handlers.
    :param context: DI container.
    :return: dict {str:handler}.
    """

    logger = logging.getLogger()
    logger.setLevel(logging.WARNING)

    async def command_handler(message: Message) -> None:
        commands = {
            "print": services.output_message,
            "send": services.send_message_to_web,
        }
        async with message.process():
            cmd = message.body.decode("utf8")
            if cmd not in commands:
                logger.error("Command is not exists.")
                return
            tg_message = await services.get_message(context)
            await commands[cmd](context, tg_message)

    async def bot_message_handler(message: Message) -> None:
        async with message.process():
            try:
                data = json.loads(message.body.decode("utf8"))
                # dataclass factory
                retort = Retort()
                tg_message = retort.load(data, TgMessage)
                await services.output_message(context, tg_message)
                await services.set_message(context, tg_message)
            except json.JSONDecodeError:
                msg = f"JSONDecodeError. Message: {data}"
                logger.warning(msg)

    return {"commands": command_handler, "bot": bot_message_handler}
