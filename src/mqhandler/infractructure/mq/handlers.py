import aio_pika.abc


def get_handlers() -> dict:
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
