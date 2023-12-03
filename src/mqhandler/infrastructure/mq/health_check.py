import asyncio
import sys
import time

import aio_pika
from aiormq import AMQPConnectionError

from mqhandler.adapters.settings import SettingsRepo


async def check_connection():
    """
    Check the connection to the URL.
    If successful, exit the program with code 0, if not, then 1.
    """
    settings = SettingsRepo()

    address = await settings.get("AMQP_ADDRESS", raise_exc=True)
    port = await settings.get("AMQP_PORT", raise_exc=True)
    user = await settings.get("AMQP_USER", raise_exc=True)
    password = await settings.get("AMQP_PASSWORD", raise_exc=True)

    url = f"ampq://{user}:{password}@{address}:{port}/"

    rollback = 1
    while rollback <= 16:
        try:
            await aio_pika.connect_robust(url)
            print("Successfully connection")
            sys.exit(0)
        except AMQPConnectionError:
            print(f"Connection failed. Try again after {rollback} sec.")
            time.sleep(rollback)
            rollback *= 2
    print("Connection filed. Exit.")
    sys.exit(1)


if __name__ == "__main__":
    asyncio.run(check_connection())
