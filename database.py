# import dependencies
import asyncio
from sqlmodel import SQLModel
import asyncmy 
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
import models


# create asynchronous engine
database_url ="mysql+asyncmy://blogger_app:angelcode1234567@127.0.0.1:3306/my_blog"
async_engine = create_async_engine(database_url, echo= True) 


# create an async session factory
AsyncSessionLocal = async_sessionmaker(bind=async_engine, class_=AsyncSession, autoflush= False) 


# function to get a session
async def get_db():
    async with AsyncSessionLocal() as session:
        yield  session
        
        
# function to create tables
async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    await async_engine.dispose()
     
        
# async function
def main():
    asyncio.run(create_tables())


if __name__ == "__main__":
    main() 
  