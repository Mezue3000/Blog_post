# import vital dependencies
from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional


# *******************User Model Schemas*************************

# base schema for common fields
class UserBase(SQLModel):
    first_name: str = Field(..., max_length=25)
    last_name: str = Field(..., max_length=25)
    username: str = Field(..., max_length=50)
    email: str = Field(..., max_length=75)
    country: str = Field(..., max_length=25)
    city: str = Field(..., max_length=25)
    

# schema for creating a user
class UserCreate(UserBase):
    password: str = Field(..., min_length=12)
    confirm_password = Field(..., min_length=12)  
    
    
# schema for reading a user
class UserRead(UserBase):
    user_id: int
    created_at: datetime
    

# token schema
class Token(SQLModel):
    access_token: str
    token_type: str    


# token data schema 
class TokenData(SQLModel):
    username: Optional[str] = None
    
    
# # schema for updating a user information
# class UserUpdate(SQLModel):
#     first_name: Optional[str] = None
#     last_name: Optional[str] = None
#     username: Optional[str] = None
#     email: Optional[str] = None
#     country: Optional[str] = None
#     city: Optional[str] = None
    
   
# schema for updating user password 
class UserPasswordUpdate(SQLModel):
    old_password: str = Field(min_length=12)
    new_password: str = Field(min_length=12)
    confirm_password: str = Field(min_length=12) 
    

# *****************************Post Model schemas************************************
# schema to create post
class PostCreate(SQLModel):
    title: str = Field(..., max_length=125)
    content: str = Field(..., max_length=450)
    user_id: int  
       

# schema to read post
class PostRead(SQLModel):
    post_id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime
    user_id: int
    
  
# schema to update post  
class PostUpdate(SQLModel):
    title: Optional[str] = None
    content: Optional[str] = None
    
    
# ***************************Comment Schemas*******************************

# schema to create comment
class CommentCreate(SQLModel):
    content: str = Field(..., max_length=450) 
    post_id: int
    
    
# schema to read comment
class CommentRead(SQLModel):
    comment_id: int
    content: str
    created_at: datetime
    updated_at: datetime
    post_id: int
    
    
# schema to update comment
class CommentUpdate(SQLModel):
    content: Optional[str] = None
    
    


