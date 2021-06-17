import toml
from .info import PROJECT_ROOT


CONFIGS_PATH = PROJECT_ROOT / "configs"
APP_CONFIGS = toml.load(CONFIGS_PATH / "app.toml")["app"]
