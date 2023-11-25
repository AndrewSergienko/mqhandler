from dataclasses import dataclass

from mqhandler.adapters.settings import SettingsProto


@dataclass
class Context:
    """Dataclass that contains layer dependencies"""

    settings: SettingsProto
