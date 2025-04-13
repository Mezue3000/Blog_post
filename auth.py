# import necessary dependencies
import secrets
from datetime import datetime, timedelta, timezone
from passlib.context import CryptContext
import jwt
from jwt import PyJWTError, ExpiredSignatureError
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlmodel.ext.asyncio.session import AsyncSession
from models import User
from database import get_db
from schemas import TokenData
from typing import Optional
from sqlmodel import select



# define jwt params
SECRET_KEY = secrets.token_urlsafe(48)
ALGORITHM = "ES256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# initialize crypt context
pwd_context = CryptContext(schemes=["argon2"], default="argon2")


# function to hash password
async def hash_password(password):
    return pwd_context.hash(password)


# function to verify password
async def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)       


# function to create jwt access token 
async def create_access_token(data: dict, expire_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + (expire_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp" : expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm = ALGORITHM)  
    

# function to get current user
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

async def get_current_user(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)):
    credential_exception = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED, 
        detail = "Invalid credentials", 
        headers = {"www.Authenticate" : "Bearer"})
    
    expired_token_error = HTTPException(
        status_code = status.HTTP_401_UNAUTHORIZED,
        detail = "Token has expired",
        headers = {"WWW-Authenticate": "Bearer"})
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        username: Optional[str] = payload.get("sub")
        if username is None:
            raise credential_exception
        token_data = TokenData(username=username)
        
    except ExpiredSignatureError:
        raise expired_token_error
        
    except jwt.PyJWTError:
        raise credential_exception 
    
    statement = select(User).where(User.username == token_data.username)
    result = await db.exec(statement)
    user = result.one_or_none()
    
    if user is None:
        raise credential_exception
    return user
      
    
        