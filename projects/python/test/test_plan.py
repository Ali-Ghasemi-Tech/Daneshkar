import unittest
from modules import input_getter
from subscribe import Subscribe
from bank_account import BankAccount
from unittest.mock import patch

account = BankAccount("meli" , "ali" , 1000 , "ali_pass" , 144)

sub = Subscribe({"subscription" : "bronze" } , account)
class TestSubscription(unittest.TestCase):

    def test_plan_silver(self):
        with patch.object(__builtins__ , "input" , lambda _:1):
            self.assertEqual(sub.plan() , [{"subscription" : "silver"} , account])

    def test_plan_golden(self):
        with patch.object(__builtins__ , "input" , lambda _: 2):
            self.assertEqual(sub.plan() , [{"subscription" : "golden"} , account])

if __name__ == "__main__":
    unittest.main()
