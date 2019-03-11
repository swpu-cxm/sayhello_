from create_db import db, Message
from datetime import datetime


def update(name, body):
    message = Message(name=name, body=body, timestamp=datetime.now())
    db.session.add(message)
    db.session.commit()


def select():
    message = Message.query.order_by(Message.timestamp.desc())
    return message


def get_count():
    count = Message.query.count()
    return count
