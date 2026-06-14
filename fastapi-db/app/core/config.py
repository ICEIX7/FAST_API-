from pydantic import Extra
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # กำหนด Default ได้เฉพาะข้อมูลที่ไม่ใช่ความลับ
    PROJECT_NAME: str = "My FastAPI Project"

    # Pydantic จะบังคับให้ไปหาค่านี้จากไฟล์ .env เท่านั้น ถ้าหาไม่เจอโปรแกรมจะ Error
    DATABASE_URL: str

    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    model_config = {
        "env_file": ".env",
        "extra": Extra.ignore,
        # "env_file_encoding": "utf-8",
    }


settings = Settings()
