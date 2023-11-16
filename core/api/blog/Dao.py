from sqlalchemy.orm import Session
from .Models import Blogs
from .Schema import BlogCreate


def create_blog(db: Session, blog: BlogCreate):
    db_blog = Blogs(
        blog_id=blog.blog_id,
        title=blog.title,
        author=blog.author,
        is_public=blog.is_public
    )
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog
