import os
from typing import Protocol


class SettingsProto(Protocol):
    async def get(self, name: str, raise_exc=False) -> str | None:
        """
        Get setting parameter by name.
        :param name: The parameter name.
        :param raise_exc: If True,
         raise a ValueError if the parameter does not exist.
        :return: The value of the parameter or None if it does not exist.
        """
        pass


class SettingsRepo(SettingsProto):
    async def get(self, name: str, raise_exc=False) -> str | None:
        value = os.environ.get(name)
        if not raise_exc:
            return value
        raise ValueError(f"The setting named {name} does not exist")
