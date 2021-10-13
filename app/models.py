from flask_login import UserMixin
from .db_management import get_user


class UserData:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class UserModel(UserMixin):
    def __init__(self, user_data):
        """
        :param user_data: UserData
        """
        self.id = user_data.username
        self.password = user_data.password

    @staticmethod
    def query(username):
        user = get_user(username)
        user_data = UserData(
            username=username,
            password=user.password
        )
        return UserModel(user_data)
