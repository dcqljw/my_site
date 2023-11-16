from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .Dao import create_blog
from api.blog.Schema import BlogCreate
from config.get_db import get_db

router = APIRouter(prefix="/blog")


@router.get("/")
def test(db: Session = Depends(get_db)):
    create = BlogCreate(blog_id='123123', title="test", author="dcq", content="test", is_public=True, )
    create_blog(db, create)
    return {"code": "200"}
