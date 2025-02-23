# import dependencies
from __future__ import annotations
from sqlmodel import SQLModel, Field, Relationship, func
from typing import Optional, List
from datetime import datetime, timezone




# create user model
class User(SQLModel, table= True):
    user_id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str = Field(..., max_length=25, index=True)
    last_name: str = Field(..., max_length=25)
    email: str = Field(..., max_length=50, unique=True)
    password_hash: str = Field(...)
    country: str = Field(..., max_length=25)
    city: str = Field(..., max_length=25)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False)
    # add relationship
    posts : List[Post] = Relationship(back_populates= "user")


# create post model 
class Post(SQLModel, table=True):
    post_id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(..., max_length=125, index=True)
    content: str = Field(..., max_length=450)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), sa_column_kwargs= {'onupdate': func.now()},nullable=False)
    user_id: int = Field(
        foreign_key= "user.user_id", sa_relationship_kwargs={
        "onupdate": "CASCADE", "ondelete": "NO ACTION"})
    # add relationship
    user: User = Relationship(back_populates= "posts")
    comments: List[Comment] = Relationship(back_populates= "post")


# create comment model
class Comment(SQLModel, table=True):
     comment_id: Optional[int] = Field(default=None, primary_key=True)
     content: str = Field(..., max_length=450, index=True)
     created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), nullable=False)
     
     updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), sa_column_kwargs={"onupdate": func.now()}, nullable=False)
     
     post_id: int = Field(
        foreign_key= "post.post_id", sa_relationship_kwargs={
        "onupdate": "CASCADE", "ondelete": "NO ACTION"})
     post: Post = Relationship(back_populates= "comments")