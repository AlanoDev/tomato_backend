from peewee import *
from tomato.config import settings
import datetime;

def init_database():
    db = MySQLDatabase(settings.DATABASE.NAME, host=settings.DATABASE.HOST,
                       port=settings.DATABASE.PORT, user=settings.DATABASE.USERNAME, passwd=settings.DATABASE.PASSWORD,charset = 'utf8')
    if db.is_connection_usable():
        return db
    else:
        db.connect()
    return db

 
class BaseModel(Model):   # peewee框架提供的基本模型
    created_date = DateTimeField()
    updated_date = DateTimeField(default=datetime.datetime.now)
    class Meta:
        database = init_database()
        table_settings = ['ENGINE=InnoDB', 'DEFAULT CHARSET=utf8']
