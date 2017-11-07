from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager


class People(UserMixin, db.Model):
    """
    Create an Employee table
    """

    # Ensures table will be named in plural and not in singular
    # as is the name of the model
    __tablename__ = 'people'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    department_id = db.Column(db.Integer, db.ForeignKey('companies.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    is_admin = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        """
        Prevent pasword from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Employee: {}>'.format(self.username)

# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return People.query.get(int(user_id))


class Vendor(db.Model):
    """
    Create a Vendor table
    """

    __tablename__ = 'companies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    employees = db.relationship('people', backref='vendor',
                                lazy='dynamic')

    def __repr__(self):
        return '<Vendor: {}>'.format(self.name)


class Role(db.Model):
    """
    Create a Role table
    """

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    people = db.relationship('People', backref='role',
                                lazy='dynamic')

    def __repr__(self):
        return '<Role: {}>'.format(self.name)


class Thing(db.Model):
    """
    Create a Thing table 
    for physical objects
    """

    __tablename__ = 'thing'

    id = db.Column(db.Integer, primary_key=True)
    barcode = db.Column(db.String(64), unique=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(1024))
    owner = db.Column(db.String(255))
    barcode = db.relation('Images', backref='barcode',
                          lazy='dynamic')
    owner = db.relation('Company', backref='owner',
                        lazy='dynamic')

    def __repr__(self):
        return '<Item>: {}'.format(self.name)

class Image(db.Model):
    """
    Create an Image Table
    for paths to the image files
    for the images of Things
    """

    __tablename__ = 'image'

    id = db.Column(db.INT, primary_key=True)
    image_path = db.Column(db.String(2048))
    item = db.relation('Thing', backref='id',
                       lazy='dynamic')
