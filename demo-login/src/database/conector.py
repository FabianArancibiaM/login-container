from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, BLOB, LargeBinary, BINARY
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "db.sqlite3")
engine = create_engine("sqlite:///"+db_path, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

class Users(Base):
    __tablename__ = 'users'
    users_id = Column(Integer, primary_key=True)
    user_name = Column(String(80), unique=True, nullable=False)
    user_password = Column(Integer, unique=True, nullable=False)

    def __init__(self, name=None, password=None, users_id=None):
        self.user_name = name
        self.user_password = password
        self.users_id = users_id

def get_users(user):
    print(BASE_DIR)
    usr = None
    usr = Users.query.filter_by(user_name=user).first()
    if usr is None:
        return None
    return Users(usr.user_name, usr.user_password, usr.users_id)