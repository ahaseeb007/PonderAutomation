import time
import pytest
from config.config import config
from pageObjects.MetaMaskPage import MetaMaskPage
from pageObjects.TransactionsPage import TransactionsPage
from testCase.test_base import BaseTest

class TestTransactions(BaseTest):

    @pytest.mark.run(order=2)
    def test_transaction(self):
        self.mp = MetaMaskPage(self.driver)
        self.mp.click_connect_wallet()
        self.mp.click_meta_mask_button()
        self.mp.switch_to_meta_mask()
        self.mp.enter_password(config.meta_password)
        self.mp.click_unblock_btn()
        self.mp.switch_window()
        self.mp.validate_connection()

        self.tp= TransactionsPage(self.driver)
        self.tp.click_from_chain_bsc()
        self.tp.click_from_chain_token_bnb()
        self.tp.click_to_chain_bsc()
        self.tp.click_to_chain_token_ustd()
        self.tp.input_token_amount("0.001")
        self.tp.click_accept_button()
        self.mp.switch_to_meta_mask()
        self.mp.click_next_btn()
        self.mp.validate_transaction_successful()