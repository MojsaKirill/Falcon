import json
from model import User


class UserController:

    def __init__(self, sessionmaker):
        self.sessionmaker=sessionmaker

    def on_get(self, req, resp):
        session = self.sessionmaker()
        user = User("Kirill", "kirill_mojsa@mail.ru", "password")
        session.add(user)
        session.commit()
        content = {
            'name': user.name,
            "fullname": user.fullname,
            "password": user.password,
        }
        resp.body = json.dumps(user.__repr__())
