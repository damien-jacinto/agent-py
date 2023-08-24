import os


class Config:
    TITLE: str = "Agent"
    ENV: str = "development"
    DEBUG: bool = True
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    version: str
    description: str

    def __init__(self, version: str, description: str) -> None:
        self.version = version
        self.description = description


class DevelopmentConfig(Config):
    TITLE: str = "Agent - dev"


class LocalConfig(Config):
    TITLE: str = "Agent - local"


class ProductionConfig(Config):
    DEBUG: str = False


def get_config():
    env = os.getenv("ENV", "local")
    version = os.getenv("VERSION", "1.0.0")
    description = os.getenv("DESCRIPTION", "api for python agent")
    config_type = {
        "dev": DevelopmentConfig(version, description),
        "local": LocalConfig(version, description),
        "prod": ProductionConfig(version, description),
    }
    return config_type[env]


config: Config = get_config()
