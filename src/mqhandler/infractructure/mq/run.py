import asyncio

import aio_pika

from mqhandler.infractructure.mq.handlers import get_handlers


async def run_app() -> None:
    url = "amqp://guest:guest@localhost:5672/"
    conn = await aio_pika.connect_robust(url)
    channel = await conn.channel()

    handlers = get_handlers()
    tasks = [
        run_queue_consumer(conn, channel, "commands", handlers["commands"]),
        run_queue_consumer(conn, channel, "bot", handlers["bot"]),
    ]
    await asyncio.gather(*tasks)


async def run_queue_consumer(
    connection: aio_pika.abc.AbstractRobustConnection,
    channel: aio_pika.abc.AbstractChannel,
    queue_name: str,
    handler,
) -> None:
    queue = await channel.declare_queue(queue_name, auto_delete=True)
    await queue.consume(handler, arguments={"one": 1})

    try:
        await asyncio.Future()
    finally:
        await connection.close()


if __name__ == "__main__":
    asyncio.run(run_app())
