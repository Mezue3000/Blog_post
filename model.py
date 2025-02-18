# import vital dependencies
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime
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
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)




# create post model 

