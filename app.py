import falcon
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from api.user import UserController
from database import DB_URL

engine = create_engine(DB_URL, echo=True)
sessionmaker = sessionmaker(bind=engine)

api = falcon.API()
api.add_route('/user', UserController(sessionmaker))