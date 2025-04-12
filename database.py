# import dependencies
import asyncio
from sqlmodel import SQLModel
import asyncmy 
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
import models
from dotenv import load_dotenv
import os


# load environment variable
load_dotenv()

# get database url environment variable
databaseUrl = os.getenv('database_url')


# create asynchronous engine
async_engine = create_async_engine(databaseUrl, echo= True)  


# create an async session factory
AsyncSessionLocal = async_sessionmaker(bind = async_engine, class_ = AsyncSession, autoflush = False) 


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
  