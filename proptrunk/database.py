from sqlalchemy import Column, Integer, String
from sqlalchemy import Model, DateTime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


"""
Model Defintions
"""

"""
Person

id
username
first_name
last_name
email
phone
mailing_address
city
state
zip
"""
class Person(Base):
    __tablename__ = 'Person'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone = Column(String)
    mailing_address  = Column(String)
    city = Column(String)
    state = Column(String)
    zip = Column(String)

"""
Item

id
name
description
location
size
owner
key_words
genre
era
"""
class Item(Base):
    __tablename__ = 'Item'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    owner = Column(Integer)
    location = Column(String, nullable=False)
    key_words = Column(String)
    genre = Column(String)
    era = Column(String)

"""
History

id
date
action
item
commiter
"""
class History(Base):
    __tablename__ = 'History'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    action = Column(String)  # Should be ENUM
    item = Column(Integer)
    commiter = Column(Integer)
    # Insert foreign keys here

"""
Checkout

id
outdate
indate
commiter
order_number
"""
class CheckedOut(Base):
    __tablename__ = 'CheckedOut'

    id = Column(Integer, primary_key=True)
    checkout_date = Column(DateTime)
    return_date = Column(DateTime)
    commiter = Column(Integer)
    order_number = Column(Integer)
    # Insert foreign key here (user ID)

class CheckIn(Base):
    __tablename__ = 'CheckIn'

    id = Column(Integer, primary_key=True)
    checkin_date = Column(DateTime)
    # mode foreign keys here

"""
Order

id
item_number
...
"""
class Order(Base):
    __tablename__ = 'Order'

    id = Column(Integer, primary_key=True)
    order_number = Column(Integer)
    item = Column(Integer)
    # List of items
    # for whom
    #

"""
Reservation

id
item
requestor
date
"""

class Reservation(Base):
    __tablename__ = 'Reservation'

    id = Column(Integer, primary_key=True)
    res_number = Column(Integer)
    item = Column(Integer)
    requestor = Column(Integer)
    date = Column(DateTime)
    # Foredign keys here (Item ID)


"""
Database Access Functions
"""

def connect():
    # Connect to the Database
    # return a connection
    retval = create_engine()
    return

def create():
    # Create the database if it doesn't exist
    foo = connect
    for model in models:

    return
