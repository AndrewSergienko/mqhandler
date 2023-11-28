import concurrent.futures
from typing import Protocol


class OutputProto(Protocol):
    async def info(self, msg: str) -> None:
        """Display the message on the screen."""
        pass


class OutputAdapter(OutputProto):
    def __init__(self):
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)

    async def info(self, msg: str) -> None:
        self.executor.submit(print, msg)
