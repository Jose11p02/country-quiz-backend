import os
from dotenv import load_dotenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy import create_engine

load_dotenv()

TURSO_DATABASE_URL=os.getenv('TURSO_DATABASE_URL')

TURSO_AUTH_TOKEN=os.getenv('TURSO_AUTH_TOKEN')

if not TURSO_DATABASE_URL or not TURSO_AUTH_TOKEN:
    raise ValueError("The 'TURSO_DATABASE_URL' and 'TURSO_AUTH_TOKEN' variables must be set.")

#sqlite_file_name = "../database.sqlite"
#base_dir = os.path.dirname(os.path.realpath(__file__))

database_url = f"sqlite+{TURSO_DATABASE_URL}?authToken={TURSO_AUTH_TOKEN}&secure=true"

engine = create_engine(database_url,echo=True)

session_local = sessionmaker(bind=engine)

base = declarative_base()