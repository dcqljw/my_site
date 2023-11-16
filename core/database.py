from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+pymysql://dcq:Dcq.159357@47.108.222.236/my_site?charset=utf8', pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
