from sqlalchemy import Column, Integer, String, DateTime, func, Text

from database import Base


class Blogs(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True)
    blog_id = Column(String(50), nullable=False)
    title = Column(String(100), nullable=False)
    author = Column(String(20), nullable=False)
    create_datetime = Column(DateTime, nullable=False, default=func.now())
    is_public = Column(Integer, nullable=False, default=1)


class BlogText(Base):
    __tablename__ = 'blog_text'
    blog_id = Column(Integer, primary_key=True)
    html_text = Column(Text, nullable=False)
    md_text = Column(Text, nullable=False)
