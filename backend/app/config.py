from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    arango_host: str = "http://localhost:8529"
    arango_db: str = "weather"
    arango_user: str = "root"
    arango_password: str = "password"
    weather_api_key: str = ""

    class Config:
        env_file = ".env"


settings = Settings()
