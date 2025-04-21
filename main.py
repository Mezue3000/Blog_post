# import neccessary dependencies
from fastapi import FastAPI
from routes import login, users

# initialize fastapi
app = FastAPI()

# include all routers
app.include_router(users.router)
app.include_router(login.router)
