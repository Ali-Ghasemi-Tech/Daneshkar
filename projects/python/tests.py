import unittest
from manager import Manager
from subscribe import Subscribe
from modules import input_getter
from bank_account import BankAccount
from unittest.mock import patch
from modules import validBank , isDigit , password

account = BankAccount("meli" , "ali" , 1000 , "ali_pass" , 144)

mock_user_account= {
                "user_name": "ali" ,
                "user_pass": password.hash_password("ali_pass") ,
                "user_phone": None ,
                "user_id": 1 ,
                "date_of_birth" : 1379/7/9 ,
                "age" : 24 ,
                "creation_date" : 2024/1/1,
                "bank_accounts" : [account],
                "wallet_balance" : 0,
                "subscription" : "bronze",
                }

sub = Subscribe({"subscription" : "bronze" } , account)
class TestSubscription(unittest.TestCase):

    def test_plan_silver(self):
        with patch.object(__builtins__ , "input" , lambda _:1):
            self.assertEqual(sub.plan() , [{"subscription" : "silver"} , account])

    def test_plan_golden(self):
        with patch.object(__builtins__ , "input" , lambda _: 2):
            self.assertEqual(sub.plan() , [{"subscription" : "golden"} , account])

class TestManager(unittest.TestCase):
    def setUp(self):
        self.user_account = {"user_name": "test_user"}
        self.bank_accounts = []

    def tearDown(self):
        self.bank_accounts = []

    def test_create_account(self):
        with patch.object(validBank, 'get_bank', return_value='Test Bank'):
            with patch.object(password, 'get_password', return_value='test_password'):
                with patch.object(isDigit, 'get_initial_amount', return_value=100):
                    with patch.object(isDigit , 'get_cvv2' , return_value = 444):
                        manager = Manager(self.user_account, self.bank_accounts)
                        new_account = manager.create_account()

                        self.assertIsInstance(new_account, BankAccount)
                        self.assertEqual(new_account.bank, 'Test Bank')
                        self.assertEqual(new_account.name, 'test_user')
                        self.assertEqual(new_account._balance, 100)
                        self.assertEqual(new_account.password, password.hash_password
                        ('test_password'))
                        self.assertEqual(new_account.cvv2 , 444)
                        self.assertIn(new_account, self.bank_accounts)


        

if __name__ == "__main__":
    unittest.main()
