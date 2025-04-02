from passlib.context import CryptContext 



pwd_context = CryptContext(schemes=["argon2"], default="argon2")


# function to hash password
async def hash_password(password):
    return pwd_context.hash(password)


# function to verify password
async def verify_password(plain_password, hashed_password):
    pwd_context.verify(plain_password, hashed_password)