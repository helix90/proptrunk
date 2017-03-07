from sqlalchemy import column, Integer, String
from sqlalchemy import Model, DateTime

class Person(Model):
    id = column(Integer, primary_key=True)
    username = column(String)
    email = column(String)
    phone = column(String)

class Item(Model):
    id = column(Integer, primary_key=True)
    name = column(String)
    description = column(String)

class History(Model):
    id = column(Integer, primary_key=True)
    # Insert foreign keys here

class CheckedOut(Model):
    id = column(Integer, primary_key=True)
    checkout_date = column(DateTime)
    # Insert foreign key here (user ID)

class CheckIn(Model):
    id = column(Integer, primary_key=True)
    checkin_date = column(DateTime)
    # mode foreign keys here

class Order(Model):
    id = column(Integer, primary_key=True)
    # List of items
    # for whom
    #

class Reservation(Model):
    id = column(Integer, primary_key=True)
    # Foredign keys here (Item ID)

def connect():
    # Connect to the Database
    # return a connection

