import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy import create_engine

sqlite_file_name = "../database.sqlite"
base_dir = os.path.dirname(os.path.realpath(__file__))

database_url = f"sqlite:///{os.path.join(base_dir,sqlite_file_name)}"

engine = create_engine(database_url)

session_local = sessionmaker(bind=engine)

base = declarative_base()