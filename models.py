# import dependencies
from __future__ import annotations
from sqlmodel import SQLModel, Relationship, func
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional, List
from datetime import datetime, timezone


# create user model
class User(SQLModel, table= True):
    __tablename__ = "users"
    
    user_id: Mapped[Optional[int]] = mapped_column(default=None, primary_key=True)
    first_name: Mapped[str ]= mapped_column(max_length=25, nullable=False)
    last_name: Mapped[str] = mapped_column(max_length=25, nullable=False)
    username: Mapped[str] = mapped_column(max_length=55, unique=True, nullable=False, index=True) 
    email: Mapped[str] = mapped_column(max_length=55, unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(max_length=255, nullable=False)
    country: Mapped[str] = mapped_column(max_length=25, nullable=False)
    city: Mapped[str] = mapped_column(max_length=25, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        default_factory=lambda: datetime.now(timezone.utc),
        nullable=False)
    # add relationship
    posts : Mapped[List[Post]] = Relationship(back_populates= "user") 
    

# create post model 
class Post(SQLModel, table=True):
    __tablename__ = "posts"
    
    post_id: Mapped[Optional[int]] = mapped_column(default=None, primary_key=True)
    title: Mapped[str] = mapped_column(max_length=125, index=True, nullable=False)
    content: Mapped[str] = mapped_column(max_length=450, nullable=False)
    created_at: Mapped[datetime] = mapped_column(default_factory=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        default_factory=lambda: datetime.now(timezone.utc), sa_column_kwargs= {'onupdate': func.now()},nullable=False)
    # add foreign key
    user_id: Mapped[int] = mapped_column(foreign_key= "users.user_id") 
    # add relationship
    user: Mapped[User] = Relationship(back_populates= "posts")
    comments: Mapped[List[Comment]] = Relationship(back_populates= "post")


# create comment model
class Comment(SQLModel, table=True):
    __tablename__ = "comments"
    
    comment_id: Mapped[Optional[int]] = mapped_column(default=None, primary_key=True)
    content: Mapped[str] = mapped_column(max_length=450, index=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        default_factory=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        default_factory=lambda: datetime.now(timezone.utc), sa_column_kwargs={"onupdate": func.now()}, nullable=False)
    #  add foreign key
    post_id: Mapped[int] = mapped_column(foreign_key= "posts.post_id")
    #  add relationship
    post: Mapped[Post] = Relationship(back_populates= "comments") 
     