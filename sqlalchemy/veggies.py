from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# connect to postgres datab ase
engine = create_engine('postgresql://postgres@localhost:5432/week3')
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Veggie(Base):
    __tablename__="veggies"

    # set auto-increment to use SERIAL data type
    id = Column(Integer, primary_key=True, autoincrement=True)
    color = Column(String, nullable=False)
    name = Column(String, nullable=False)


# Recreate all tables each time script is run
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

seed_data = [
    {'name': 'carrot', 'color': 'orange'},
    {'name': 'onion', 'color': 'yellow'},
    {'name': 'zucchini', 'color': 'green'},
    {'name': 'squash', 'color': 'yellow'},
    {'name': 'pepper', 'color': 'red'},
    {'name': 'onion', 'color': 'red'}
]

# turn the seed data into a list of veggie objects
veggie_objects = []
for item in seed_data:
    v = Veggie(name=item["name"], color=item["color"])
    veggie_objects.append(v)

# create a session, insert new records, and commit the session
session = Session()
session.bulk_save_objects(veggie_objects)
session.commit()