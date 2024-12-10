from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# load env
BASE_DIR = os.path.dirname(os.path.abspath('__file__'))
load_dotenv(os.path.join(BASE_DIR, '.env'))



PSQL_USER = os.getenv("PSQL_USER")
PSQL_PASSWORD = os.getenv("PSQL_PASSWORD")
PSQL_HOST = os.getenv("PSQL_HOST")
PSQL_DB_NAME = os.getenv("PSQL_DB_NAME")
PSQL_PORT = os.getenv("PSQL_PORT")

DATABASE_URL = f"postgresql://{PSQL_USER}:{PSQL_PASSWORD}@{PSQL_HOST}:{PSQL_PORT}/{PSQL_DB_NAME}"



engine = create_engine(DATABASE_URL)
sessionLocal = sessionmaker(bind=engine)

