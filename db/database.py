import os
from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


load_dotenv()

username = os.environ.get("DATABASE_USERNAME")
password = os.environ.get("DATABASE_PASSWORD")
address = os.environ.get("DATABASE_ADDRESS")
project = os.environ.get("DATABASE_PROJECT")

database_url = f'mysql+pymysql://{username}:{password}@{address}/{project}'

engine = create_engine(url=database_url)

# Create a local session
LocalSession = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()