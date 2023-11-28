import asyncio
from typing import Any, Callable, Coroutine

import aio_pika
from aio_pika.abc import AbstractIncomingMessage

from mqhandler.infractructure.bootstrap import get_context, get_web_session
from mqhandler.infractructure.mq.handlers import get_handlers


async def run_app() -> None:
    web_session = get_web_session()
    context = get_context(web_session)

    url = await context.settings.get("AMQP_ADDRESS", raise_exc=True)
    conn = await aio_pika.connect_robust(url)
    channel = await conn.channel()

    handlers = get_handlers(context)
    tasks = [
        run_queue_consumer(channel, "commands", handlers["commands"]),
        run_queue_consumer(channel, "bot", handlers["bot"]),
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
    handler: Callable[[AbstractIncomingMessage], Coroutine[Any, Any, None]],
) -> None:
    queue = await channel.declare_queue(queue_name, auto_delete=True)
    await queue.consume(handler)


if __name__ == "__main__":
    asyncio.run(run_app())
