from . import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    phone_number = db.Column(db.Text)
    name = db.Column(db.Text)
    email = db.Column(db.Text)

class MessageType(db.Model):
    __tablename__ = 'message_types'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text)

class MediaType(db.Model):
    __tablename__ = 'media_types'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text)

class ReceivedMessage(db.Model):
    __tablename__ = 'received_messages'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    time_stamp = db.Column(db.Text)
    text_content = db.Column(db.Text)
    media_url = db.Column(db.Text)
    is_read = db.Column(db.Integer)
    media_type_id = db.Column(db.Integer, db.ForeignKey('media_types.id'))
    message_type_id = db.Column(db.Integer, db.ForeignKey('message_types.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

class SentMessage(db.Model):
    __tablename__ = 'sent_messages'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    time_stamp = db.Column(db.Text)
    text_content = db.Column(db.Text)
    media_url = db.Column(db.Text)
    is_read = db.Column(db.Integer)
    media_type_id = db.Column(db.Integer, db.ForeignKey('media_types.id'))
    message_type_id = db.Column(db.Integer, db.ForeignKey('message_types.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

class CatalogueType(db.Model):
    __tablename__ = 'catalogue_types'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text)

class Catalogue(db.Model):
    __tablename__ = 'catalogue'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text)
    description = db.Column(db.Text)
    cost_price = db.Column(db.Float)
    sell_price = db.Column(db.Float)
    catalogue_type_id = db.Column(db.Integer, db.ForeignKey('catalogue_types.id'))

class Sale(db.Model):
    __tablename__ = 'sales'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    quantity = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    catalogue_id = db.Column(db.Integer, db.ForeignKey('catalogue.id'))
