from fastapi import FastAPI
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware
# นำเข้า api_router ที่เราสร้างไว้ใน api/v1/api.py
from app.api.v1.api import api_router
from app.core.limiter import limiter
# สำหรับ Scalar API reference
from scalar_fastapi import get_scalar_api_reference

# สร้างแอปพลิเคชัน FastAPI
app = FastAPI(title="My FastAPI App")

# ตั้งค่า Limiter
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_middleware(SlowAPIMiddleware)



# นำ Router ทั้งหมดมาแปะที่ /api/v1
app.include_router(api_router, prefix="/api/v1")


# เส้นทาง API สำหรับดู Scalar API reference
# Path: /scalar
@app.get("/scalar", include_in_schema=False)
async def scalar_html():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        # title="Scalar FastAPI API Reference",
        title=app.title,
    )