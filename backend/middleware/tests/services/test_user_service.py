from services.user_service import UserService
from tests.utils import app


class TestUserService:
    @classmethod
    def setup_class(cls):
        cls.app = app

    def test_get_all_users(self):
        expected_all_users = []

        actual_all_users = UserService.get_all_users()

        assert actual_all_users == expected_all_users
