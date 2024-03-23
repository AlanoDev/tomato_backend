from peewee import *
from tomato.config import settings
import datetime;

def init_database():
    db = MySQLDatabase(settings.DATABASE.NAME, host=settings.DATABASE.HOST,
                       port=settings.DATABASE.PORT, user=settings.DATABASE.USERNAME, passwd=settings.DATABASE.PASSWORD)
    if db.is_connection_usable():
        return db
    else:
        db.connect()
    return db

 
class BaseModel(Model):
    created_date = DateTimeField()
    updated_date = DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = init_database()
