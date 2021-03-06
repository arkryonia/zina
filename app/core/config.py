import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import (
    BaseSettings,
    PostgresDsn
)


class Settings(BaseSettings):
    APP_NAME: str = "zina"
    ORIGINS: str = os.getenv("ORIGINS", "*")    

    def get_db_uri(self):
        LOCALE_DB: str = f"postgres://postgres:postgres@localhost/{self.APP_NAME}_db"
        db_uri: str = os.getenv("DATABASE_URL", LOCALE_DB)

        if db_uri.startswith("postgres://"):
            db_uri = db_uri.replace("postgres://", "postgresql://")
        return db_uri

    def init_app(self) -> FastAPI:
        app = FastAPI(
            title=f"{self.APP_NAME} API"
        )

        app.add_middleware(
            CORSMiddleware,
            allow_origins=[self.ORIGINS],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"], 
        )

        return app


settings = Settings()
