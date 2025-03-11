from sqlmodel import SQLModel, create_engine, Session


# create engine
url = "mysql+aiomysql://blogger_app:angelcode1234567@127.0.0.1:3306/my_blog"
engine = create_engine()