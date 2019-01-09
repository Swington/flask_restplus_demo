import pytest
from flask import url_for

from tests.utils import app


@pytest.mark.usefixtures('client_class')
class TestHelloWorldController:
    @classmethod
    def setup_class(cls):
        cls.app = app

    def test_hello_world_controller_returns_valid_response_on_get(self):
        expected_response = {'app': 'middleware'}
        actual_response = self.client.get(url_for('hello_hello_world'))

        assert actual_response.json == expected_response
        assert actual_response.status_code == 200
