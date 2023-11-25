from mqhandler.adapters.settings import SettingsRepo
from mqhandler.services.context import Context


def get_context() -> Context:
    return Context(SettingsRepo())
