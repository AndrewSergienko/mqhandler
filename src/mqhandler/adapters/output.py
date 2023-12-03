import concurrent.futures
from typing import Protocol, runtime_checkable


@runtime_checkable
class OutputProto(Protocol):
    async def info(self, msg: str) -> None:
        """Display the message on the screen."""
        pass


class OutputAdapter(OutputProto):
    def __init__(self):
        # Execute code in a separate thread to avoid blocking the event loop
        self.executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)

    async def info(self, msg: str) -> None:
        self.executor.submit(print, msg)
