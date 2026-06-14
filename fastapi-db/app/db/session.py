from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from app.core.config import settings

# 1. สร้าง Async Engine
engine = create_async_engine(settings.DATABASE_URL, echo=True)

# 2. สร้าง Session Factory
SessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

# 3. Dependency สำหรับใช้ใน API Endpoint (Dependency Injection)
async def get_db():
    async with SessionLocal() as session:
        yield session