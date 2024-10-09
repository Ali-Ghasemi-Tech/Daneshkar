import unittest
from Modules import input_getter
from subscribe import Subscribe
from bank_account import BankAccount

sub = Subscribe({"subscription" : "bronze" } , BankAccount("meli" , "ali" , 1000 , "ali_pass" , 144))
class TestSubscription(unittest.TestCase):

    def test_plan(self):
        input_getter.input = lambda:"1"
        return self.assertEqual(sub.plan() , {"subscription" : "silver"})

if __name__ == "main":
    unittest.main()
    TestSubscription.test_plan()