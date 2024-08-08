import pytest
from config.config import config
from pageObjects.MetaMaskPage import MetaMaskPage
from testCase.test_base import BaseTest

class TestWallet(BaseTest):
    @pytest.mark.run(order=1)
    def test_connect_wallet(self):
        self.mp = MetaMaskPage(self.driver)
        self.mp.click_connect_wallet()
        self.mp.click_meta_mask_button()
        self.mp.switch_to_meta_mask()
        self.mp.enter_password(config.meta_password)
        self.mp.click_unblock_btn()
        self.mp.switch_window()
        self.mp.validate_connection()
