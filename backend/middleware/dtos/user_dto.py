from flask_restplus import Namespace


class UserDto:
    api = Namespace('user', description='user related operations')
