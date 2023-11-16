from pydantic import BaseModel


class BlogBase(BaseModel):
    title: str
    author: str

    class Config:
        orm_mode = True


class BlogCreate(BlogBase):
    blog_id: str
    is_public: bool = True


class BlogTextBase(BaseModel):
    html_text: str
    md_text: str

    class Config:
        orm_mode = True


class BlogTextCreate(BlogTextBase):
    blog_id: int
