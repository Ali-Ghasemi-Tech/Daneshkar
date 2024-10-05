import unittest
from datetime import datetime 

users={
    '4ded782b-4d8a-4706-9941-efa3e516091f': {
        'user_name': 'ali',
        'user_pass': '719ebb43fae1c0227dbf7b88c70c0fecff93d5d626cf306a4a1e552bbdc3b172',
        'user_phone': None,
        'user_id': '4ded782b-4d8a-4706-9941-efa3e516091f',
        'date_of_birth': datetime.date(1379, 7, 9),
        'age': 24,
        'creation_date': datetime.date(2024, 10, 5),
        'bank_accounts': [],
        'subscription': 'bronze',
        }
        }

class TestAccountManager(unittest.TestCase):
    def test_getBankAccount(self):
        account = users['4ded782b-4d8a-4706-9941-efa3e516091f']
        bank_accounts = account["bank_accounts"]
        for i in bank_accounts:
                for key in i: 
                    print(i[key])
                    