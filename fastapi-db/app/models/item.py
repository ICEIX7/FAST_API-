from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .base_class import Base

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True) # รหัสสินค้า
    title = Column(String(255), nullable=False) # ชื่อสินค้า
    description = Column(String(255), nullable=True) # รายละเอียดสินค้า
    owner_id = Column(Integer, ForeignKey("users.id")) # รหัสผู้ใช้เจ้าของสินค้า

    # ความสัมพันธ์: 1 Item เป็นของ 1 User
    # back_populates จะชี้ไปที่ตัวแปร 'items' ในไฟล์ User
    owner = relationship("User", back_populates="items")
