import logging
import pytest


@pytest.mark.usefixtures("setup_api_with_auth")
class TestUser:

    def test_get_user(self, setup_api_with_auth):
        logging.info("Running test_get_user")
        response = setup_api_with_auth.get_user("testuser")
        assert response.status_code == 200

    def test_create_user(self, setup_api_with_auth):
        logging.info("Running test_create_user")
        response = setup_api_with_auth.create_user("newuser", "password")
        assert response.status_code == 201

    def test_delete_user(self, setup_api_with_auth):
        logging.info("Running test_delete_user")
        response = setup_api_with_auth.delete_user("testuser")
        assert response.status_code == 204
