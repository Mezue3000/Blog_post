# import vital dependencies
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime, timezone
from sqlalchemy import func
from __future__ import annotations


# create user model
class User(SQLModel, table= True):
    user_id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str = Field(max_length=25, nullable=False, index=True)
    last_name: str = Field(max_length=25, nullable=False)
    email: str = Field(max_length=50, unique=True, nullable=False)
    password_hash: str = Field(nullable=False)
    country: str = Field(max_length=25, nullable=False)
    city: str = Field(max_length=25, nullable=False)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False)



# create post model 
class Post(SQLModel, table=True):
    post_id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(max_length=125, nullable=False)
    content: str = Field(max_length=255, nullable=False)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc), nullable=False)
    updated_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc), sa_column_kwargs= {'onupdate': func.now},nullable=False)
    
