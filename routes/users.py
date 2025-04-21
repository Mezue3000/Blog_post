# import necessary dependencies
from fastapi import APIRouter, Depends, HTTPException, status
from schemas import UserRead, UserCreate
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from sqlmodel import select, or_
from models import User
from auth import hash_password


# initialize router
router = APIRouter(prefix="/users", tags=["users"])

# create endpoint for user registration 
@router.post("/", response_model = UserRead)  
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    # validate confirm password field
    if user.password != user.confirm_password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= "Password do not match")
    
    # check if username or email is already taken
    statement = select(User).where(or_(User.username == user.username, User.email == user.email))
    result = await db.execute(statement)
    existing_user = result.first()
    
    if existing_user:
        if existing_user.username == user.username:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already taken")
        if existing_user.email == user.email:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= "Email already taken")
    
    # create new user with hash password
    new_user = User(
        first_name = user.first_name,
        last_name = user.last_name,
        username = user.username.lower(),
        email = user.email.lower(),
        password_hash = hash_password(user.password),
        country = user.country,
        city = user.city
    ) 
    
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    
    return new_user  