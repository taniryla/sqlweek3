from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# connect to postgres datab ase
engine = create_engine('postgresql://postgres@localhost:5432/week3')
Session = sessionmaker(bind=engine)
Base = declarative_base()

