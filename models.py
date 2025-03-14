# import dependencies
from __future__ import annotations
from sqlmodel import SQLModel, Field, Relationship, func
from typing import Optional, List
from datetime import datetime, timezone


# create user model
class User(SQLModel, table= True):
    user_id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str = Field(max_length=25, nullable=False )
    last_name: str = Field(max_length=25, nullable=False)
    username: str = Field(max_length=50, nullable=False, index=True) 
    email: str = Field(max_length=50, unique=True, nullable=False)
    password_hash: str = Field(nullable=False)
    country: str = Field(max_length=25, nullable=False)
    city: str = Field(max_length=25, nullable=False)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False)
    # add relationship
    posts : List[Post] = Relationship(back_populates= "user")


# create post model 
class Post(SQLModel, table=True):
    post_id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(max_length=125, index=True, nullable=False)
    content: str = Field(max_length=450, nullable=False)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), sa_column_kwargs= {'onupdate': func.now()},nullable=False)
    # add foreign key
    user_id: int = Field(
        foreign_key= "user.user_id", sa_column_kwargs={
        "onupdate": "CASCADE", "ondelete": "NO ACTION"}) 
    # add relationship
    user: User = Relationship(back_populates= "posts")
    comments: List[Comment] = Relationship(back_populates= "post")


# create comment model
class Comment(SQLModel, table=True):
     comment_id: Optional[int] = Field(default=None, primary_key=True)
     content: str = Field(max_length=450, index=True, nullable=False)
     created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), nullable=False)
     updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), sa_column_kwargs={"onupdate": func.now()}, nullable=False)
    #  add foreign key
     post_id: int = Field(
        foreign_key= "post.post_id", sa_column_kwargs={
        "onupdate": "CASCADE", "ondelete": "NO ACTION"})
    #  add relationship
     post: Post = Relationship(back_populates= "comments")