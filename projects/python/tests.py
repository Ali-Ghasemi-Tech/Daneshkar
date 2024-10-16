import unittest
from manager import Manager
from subscribe import Subscribe
from modules import input_getter
from bank_account import BankAccount
from unittest.mock import patch
from modules import validBank , isDigit , password
from user import User
import datetime

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

sub = Subscribe({"subscription" : {"sub" : "bronze" , "used" : 0 , "date" : None}} , account)

# subscribe.py tests
class TestSubscription(unittest.TestCase):

    def test_plan_silver(self):
        with patch.object(__builtins__ , "input" , lambda _:1):
            self.assertEqual(sub.plan() , [{"subscription" : {"sub" : "silver" , "used" : 0 , "date" : datetime.datetime.now().date()}} , account])

    def test_plan_golden(self):
        with patch.object(__builtins__ , "input" , lambda _: 2):
            self.assertEqual(sub.plan() , [{"subscription" : {"sub" : "golden" , "used" : 0 , "date" : datetime.datetime.now().date()}} , account])


# manager.py tests
class TestManager(unittest.TestCase):
    def setUp(self):
        self.user_account = {"user_name": "test_user" , "wallet_balance" : 0}
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


    def test_get_bank_account(self):
        self.bank_accounts = [BankAccount("Test Bank" , "name" , 1000 , "password" , 444)]
        with patch.object(__builtins__ , "input" , lambda _:"Test Bank"):
            manager = Manager(self.user_account , self.bank_accounts)
            new_account = manager.get_bank_account()
            self.assertIsInstance(new_account , BankAccount)
            self.assertEqual(new_account.bank , 'Test Bank')
            self.assertEqual(new_account.name , 'name')
            self.assertEqual(new_account._balance , 1000)
            self.assertEqual(new_account.password , 'password')
            self.assertEqual(new_account.cvv2 , 444)

    
    def test_wallet_funds(self):
        self.bank_accounts = [BankAccount("Test Bank" , "name" , 1000 , "password" , 444)]
        manager = Manager(self.user_account , self.bank_accounts)

        with patch.object(__builtins__ , "input" , lambda _: 100):
            with patch.object(isDigit , "number_valid" , return_value= 100):
                with patch.object(__builtins__ , "input" , lambda _:"Test Bank"):
                    func = manager.wallet_funds()
                    new_account = manager.selected_bank_account
                    self.assertIsInstance(new_account , BankAccount)
                    self.assertEqual(manager.user_account['wallet_balance'] , 100)
                    self.assertEqual(func , 900)
            

# user.py tests
class TestUser(unittest.TestCase):
    def setUp(self):
        self.test_date = datetime.datetime.strptime('1380/01/01' ,"%Y/%m/%d")
        self.user = User()
        self.user_accounts = {
            '1':
            {
                'user_name' : 'Test name' ,
                'user_pass' : password.hash_password('password') 
            }

        }

    def  test_create_user(self):
        with patch.object(User , "get_user_name" , return_value = 'Test name'):
            with patch.object(password , "get_password" , return_value = 'password'):
                with patch.object(__builtins__ , "input" , lambda _: '1234'):
                    with patch.object(User , "get_birthdate" , return_value = 1380/1/1):
                        with patch.object(User , "calculate_age" , return_value = 23):
                            with patch.object(User , "id_generator" , return_value = 1):
                                user = User()
                                new_user = user.create_user()
                                self.assertEqual(new_user['user_name'] , 'Test name')
                                self.assertEqual(new_user['user_pass'] , password.hash_password('password'))
                                self.assertEqual(new_user['user_phone'] , '1234')
                                self.assertEqual(new_user['date_of_birth'] , 1380/1/1)
                                self.assertEqual(new_user['age'] , 23)

    def test_show_account(self):
        User.users = self.user_accounts
        self.user.users = self.user_accounts

        self.assertEqual(self.user.show_account('1') , self.user_accounts['1'])


    def test_get_birth_date(self):
        with patch('builtins.input' , return_value = '1380/01/01'):
            self.assertEqual(self.user.get_birthdate() , self.test_date.date())

    def test_calculate_age(self):
        self.assertEqual(self.user.calculate_age(self.test_date) , 23)

    def test_get_user_name(self):
        User.users = self.user_accounts
        with patch('builtins.input' , return_value = 'name'):
            self.assertEqual(self.user.get_user_name() , 'name')

    def test_updata_password(self):
        self.user.update_pass('new_password' , '1')
        self.assertEqual(User.users['1']['user_pass'] , 'new_password')

# bank_account.py tests
class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.bank_account = BankAccount('test bank' , 'test name' , 100 , 'password' , 444)
        self.bank_account_with_cridit  = BankAccount('test bank' , 'test name' , 2000 , 'password' , 444)

    def test_deposit(self):
        self.bank_account.deposit(10)
        self.assertEqual(self.bank_account._balance , 110)

    def test_withdraw(self):
        self.bank_account.withdraw(10)
        self.assertEqual(self.bank_account._balance , 90)

    def test_get_balance(self):
        self.assertEqual(self.bank_account.get_balance() , 100)
                   
    def test_check_cridit(self):
        self.assertEqual(self.bank_account.check_credit() , 0)
        self.assertEqual(self.bank_account_with_cridit.check_credit() , 1)
if __name__ == "__main__":
    unittest.main()
