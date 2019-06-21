from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from SessionHolder import init_session
from model.user import User

DB_URL = "postgresql://postgres:postgres@localhost:5432/falcon"

init_session(DB_URL)

user = User("Kirill", "Moysa", "qwe123")

sql = session.query(User).filter(User.id == 3).one()
print(sql)