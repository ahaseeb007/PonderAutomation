import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TransactionsPage:

    bsc_xpath= "//span[contains(text(), 'BSC')]"
    bsc_to_xpath= "//div[@class='c-hegpaq c-hVeQuS c-hegpaq-brNQLi-shadow-lightGray c-hegpaq-ikNCflu-css']//div[@class='c-dhzjXW c-dhzjXW-iTKOFX-direction-column c-dhzjXW-jroWjL-align-center c-dhzjXW-awKDG-justify-start c-dhzjXW-kVNAnR-wrap-noWrap']"
    bnb_image_css= "img.c-ezVtOj.c-ezVtOj-ijNtXOL-css[src='https://assets.coingecko.com/coins/images/825/small/binance-coin-logo.png?1547034615']"
    bnb_token_xpath = "//span[contains(text(), 'BNB')]"
    dai_token_xpath= "//span[contains(text(), 'DAI')]"
    ustd_token_xpath= "//span[contains(text(), 'USDT')]"
    enter_password_field_ID= "password"
    click_unlock_btn_xpath= "//button[@data-testid='unlock-submit']"
    ethereum_chain_xpath= "//span[normalize-space()='Ethereum']"
    click_confirm_btn_css= ".btn--rounded.btn-primary"
    connect_wallet_xpath= "//button[normalize-space()='Connect Wallet']"
    accept_button_xpath= "//button[normalize-space()='Accept']"
    input_amount_xpath= "//input[@placeholder='Enter Amount']"
    fund_error_xpath= "//span[contains(@class, 'c-dXbppQ') and contains(@class, 'c-dXbppQ-kQlCNI-color-purple') and text()='You do not have enough funds to complete the transaction.']"

    def __init__(self,driver):
        self.driver= driver

    def simulate_mouse_movement(self, driver):
        actions = ActionChains(driver)

        wait = WebDriverWait(self.driver, 10)

        element = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.bsc_xpath)))

        # Move to the element
        actions.move_to_element(element)

        # Small random movements to simulate human-like behavior
        actions.move_by_offset(10, 10).pause(1)
        actions.move_by_offset(-5, -5).pause(0.5)

        # Perform the actions
        actions.perform()

        # Pause to ensure the movements are registered
        time.sleep(2)


    def click_from_chain_bsc(self):
        try:
            wait = WebDriverWait(self.driver, 10)
            click_bsc_chain = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.bsc_xpath)))
            click_bsc_chain.click()
            click_bsc_chain.click()
            time.sleep(5)
        except:
            assert False, "From BSC chain button is not visible"

    def click_from_chain_token_bnb(self):
        try:
            wait = WebDriverWait(self.driver, 20)
            click_bnb_token = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.bnb_token_xpath)))
            click_bnb_token.click()
        except:
            assert False, "From Chain BNB token button is not visible"

    def click_to_chain_bsc(self):
        try:

            wait = WebDriverWait(self.driver, 20)
            click_bsc_chain = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.bsc_to_xpath)))
            click_bsc_chain.click()
            click_bsc_chain.click()
        except:
            assert False, "To BSC chain button is not visible"

    def click_to_chain_token_dai(self):
        try:
            wait = WebDriverWait(self.driver, 20)
            click_bnb_token = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.dai_token_xpath)))
            click_bnb_token.click()
        except:
            assert False, "To DAI token button is not visible"

    def click_to_chain_token_ustd(self):
        try:
            wait = WebDriverWait(self.driver, 20)
            click_bnb_token = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.ustd_token_xpath)))
            click_bnb_token.click()
        except:
            assert False, "To USDT token button is not visible"

    def input_token_amount(self, token_amount):
        try:
            wait = WebDriverWait(self.driver, 20)
            input_amount = wait.until(
            EC.presence_of_element_located((By.XPATH, self.input_amount_xpath)))
            input_amount.send_keys(token_amount)
        except:
            assert False, "Input amount field is not visible"

    def click_accept_button(self):
        try:
            wait = WebDriverWait(self.driver, 30)
            accept_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, self.accept_button_xpath)))
            accept_button.click()
            time.sleep(10)
        except:
            assert False, "Accept button not visible or clickable"
