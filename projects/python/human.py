
class Human:
    users : dict = {}

    def get_user_name(self) -> str :
        """gets user_name from dict and if the user_name already exist then retruns itself until the input user_name does not exist
        
        return string"""
        user_name : str = input("please enter username: ")
        name_exist : bool = self._check_username(user_name)
        if name_exist:
            print("\nthis user_name already exists , please enter another user_name! (╥‸╥) \n")
            return self.get_user_name()
        return user_name
    

    def _check_username(self , new_user_name) -> bool:
        """check if the user_name exist in the users
        
        returns boolian"""
        for id in Human.users:
            if Human.users[id]["user_name"] == new_user_name:
                return True
        
        return False