import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
sqlite_file_name = "../database.sqlite"

base_dir = os.path.dirname(os.path.realpath(__file__))

db_url = f"sqlite:///{os.path.join(base_dir,sqlite_file_name)}"

engine_db = create_engine(db_url,echo=True)

Session = sessionmaker(autoflush=False,bind=engine_db)

Base = declarative_base()