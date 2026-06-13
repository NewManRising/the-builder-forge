from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    model_path: str = "models/Gradient_Boosting.pkl"

    class Config:
        env_file = ".env"


settings = Settings()
