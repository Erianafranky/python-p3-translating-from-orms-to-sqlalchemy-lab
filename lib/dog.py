from models import Dog
from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:')

def create_table(base, engine):
    base.metadata.create_all(engine)
    return engine

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    dogs = session.query(Dog).all()
    return dogs

def find_by_name(session, name):
    query = session.query(Dog).filter(Dog.name == name).first()
    return query

def find_by_id(session, id):
    query = session.query(Dog).filter(Dog.id == id).first()
    return query

def find_by_name_and_breed(session, name, breed):
    query = session.query(Dog).filter(Dog.name == name and Dog.breed == breed).first()
    return  query

def update_breed(session, dog, breed):
    query = session.query(Dog).filter(Dog.id == dog.id).update({Dog.breed: breed})
    return query