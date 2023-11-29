from dataclasses import asdict
from pathlib import Path

from mqhandler.domain.dto import TgMessage
from mqhandler.services.context import Context


async def output_message(context: Context, message: TgMessage) -> None:
    await context.output.info(str(message))


async def send_message_to_web(context: Context, message: TgMessage) -> None:
    url = await context.settings.get("EXTERNAL_API_URL", raise_exc=True)
    await context.web.post(url or "", asdict(message))


async def set_message(context: Context, message: TgMessage) -> None:
    file_path = await message_file_path(context)
    await context.message.set_message(file_path, message)


async def get_message(context: Context) -> TgMessage:
    file_path = await message_file_path(context)
    return await context.message.get_message(file_path)


async def message_file_path(context: Context) -> Path:
    file_path = await context.settings.get("FILE_PATH", raise_exc=True) or ""
    return context.root_path / file_path
