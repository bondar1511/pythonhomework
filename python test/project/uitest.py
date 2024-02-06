import logging
import pytest


@pytest.mark.usefixtures("setup_ui")
class TestLogin:

    def test_successful_login(self, setup_ui):
        logging.info("Running test_successful_login")
        setup_ui.login("testuser", "password")
        assert setup_ui.is_logged_in()

    def test_failed_login(self, setup_ui):
        logging.info("Running test_failed_login")
        setup_ui.login("invaliduser", "password")
        assert not setup_ui.is_logged_in()
