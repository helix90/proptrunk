from sqlalchemy import column, Integer, String
from sqlalchemy import Model, DateTime


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
class Person(Model):
    id = column(Integer, primary_key=True)
    username = column(String)
    first_name = column(String)
    last_name = column(String)
    email = column(String)
    phone = column(String)
    mailing_address  = column(String)
    city = column(String)
    state = column(String)
    zip = column(String)

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
class Item(Model):
    id = column(Integer, primary_key=True)
    name = column(String)
    description = column(String)
    owner = column(Integer)
    location = column(String, nullable=False)
    key_words = column(String)
    genre = column(String)
    era = column(String)

"""
History

id
date
action
item
commiter
"""
class History(Model):
    id = column(Integer, primary_key=True)
    date = column(DateTime)
    action = column(String)  # Should be ENUM
    item = column(Integer)
    commiter = column(Integer)
    # Insert foreign keys here

"""
Checkout

id
outdate
indate
commiter
order_number
"""
class CheckedOut(Model):
    id = column(Integer, primary_key=True)
    checkout_date = column(DateTime)
    return_date = column(DateTime)
    commiter = column(Integer)
    order_number = column(Integer)
    # Insert foreign key here (user ID)

class CheckIn(Model):
    id = column(Integer, primary_key=True)
    checkin_date = column(DateTime)
    # mode foreign keys here

"""
Order

id
item_number
...
"""
class Order(Model):
    id = column(Integer, primary_key=True)
    order_number = column(Integer)
    item = column(Integer)
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

class Reservation(Model):
    id = column(Integer, primary_key=True)
    item = column(Integer)
    requestor = column(Integer)
    date = column(DateTime)
    # Foredign keys here (Item ID)


"""
Database Access Functions
"""

def connect():
    # Connect to the Database
    # return a connection

