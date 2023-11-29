from dataclasses import dataclass
from pathlib import Path

from mqhandler.adapters.message import TgMessageProto
from mqhandler.adapters.output import OutputProto
from mqhandler.adapters.settings import SettingsProto
from mqhandler.adapters.web import WebProto


@dataclass
class Context:
    """Dataclass that contains layer dependencies."""

    settings: SettingsProto
    output: OutputProto
    web: WebProto
    message: TgMessageProto

    root_path: Path
