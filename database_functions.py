from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
import hashlib
import datetime
import random
from database_declarative import *

class Database:
    def __init__(self, dbname="amiwritedata"):
        self.engine = create_engine()
        Base.metadata.bind = self.engine
        DBSession = sessionmaker(bind=self.engine)
        self.session = DBSession()
    
    #close database
    def close(self):
        self.session.close()