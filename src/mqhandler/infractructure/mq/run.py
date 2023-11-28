import asyncio
from typing import Any, Callable, Coroutine

import aio_pika
from aio_pika.abc import AbstractIncomingMessage

from mqhandler.infractructure.bootstrap import (
    get_context,
    get_mq_url,
    get_root_path,
    get_web_session,
    logging_setup,
)
from mqhandler.infractructure.mq.handlers import get_handlers

Handler = Callable[[AbstractIncomingMessage], Coroutine[Any, Any, None]]


async def run_app() -> None:
    """Create and run message queues handlers"""

    logging_setup()

    # create DI container
    web_session = get_web_session()
    context = get_context(web_session, get_root_path())

    # connect to MQ
    url = await get_mq_url(context)
    conn = await aio_pika.connect_robust(url)
    channel = await conn.channel()

    commands_queue = (
        await context.settings.get("COMMANDS_QUEUE", raise_exc=True) or ""
    )
    bot_queue = await context.settings.get("BOT_QUEUE", raise_exc=True) or ""

    handlers = get_handlers(context)
    tasks = [
        run_queue_consumer(channel, commands_queue, handlers["commands"]),
        run_queue_consumer(channel, bot_queue, handlers["bot"]),
    ]
    await asyncio.gather(*tasks)

    try:
        await asyncio.Future()
    finally:
        # close aiohttp session and aio_pika connection
        await web_session.close()
        await conn.close()


async def run_queue_consumer(
    channel: aio_pika.abc.AbstractChannel,
    queue_name: str,
    handler: Handler,
) -> None:
    """Create task of message queue consumer"""
    queue = await channel.declare_queue(queue_name, auto_delete=True)
    await queue.consume(handler)


if __name__ == "__main__":
    asyncio.run(run_app())
