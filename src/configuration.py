import pydantic


class Settings(pydantic.BaseSettings):
    provider: str = "big-data-energy"
    output_collection: str = "konstantin-scheduled-data-time-app"
    version: int = 1


SETTINGS = Settings()