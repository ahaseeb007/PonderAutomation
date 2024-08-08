# import pytest
# from testCase.test_base import BaseTest
# from testCase.test_connect_wallet import Test_Connectwallet
# from testCase.test_transactions import TestTransactions
#
#
# @pytest.mark.usefixtures("setup")
# class TestClass(BaseTest):
#     @pytest.mark.run(order=1)
#     def test_case1(self, setup):
#         conect_wallet = Test_Connectwallet()
#         conect_wallet.connect_wallet()
#
#     @pytest.mark.run(order=2)
#     def test_case2(self, setup):
#         Test_Transactions= TestTransactions()
#         Test_Transactions.transaction()