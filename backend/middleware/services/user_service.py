import datetime
import uuid

from models import UserModel
from models import db


class UserService:
    @classmethod
    def save_new_user(cls, data):
        user = UserModel.query.filter_by(email=data['email']).first()
        if not user:
            new_user = UserModel(
                public_id=str(uuid.uuid4()),
                email=data['email'],
                username=data['username'],
                password=data['password'],
                registered_on=datetime.datetime.utcnow()
            )
            cls.save(new_user)
            response_object = {
                'status': 'success',
                'message': 'Successfully registered.'
            }
            return response_object, 201
        else:
            response_object = {
                'status': 'fail',
                'message': 'UserModel already exists. Please Log in.',
            }
            return response_object, 409

    @classmethod
    def save(cls, data):
        db.session.add(data)
        db.session.commit()

    @staticmethod
    def get_all_users():
        return UserModel.query.all()

    @staticmethod
    def get_a_user(public_id):
        return UserModel.query.filter_by(public_id=public_id).first()
