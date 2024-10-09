from getpass import getpass
import hashlib
def get_password() -> str :
        """handels getting password from user and checking it. if the password is not valid then it returns itself
        
        returns string"""
        user_pass: str = getpass("please enter passwrod: ")
        valid_pass: function = _check_password(user_pass)

        if not valid_pass:
            print("\nyour password should be atleast 4 charecters long! –_–)#\n")
            return get_password()
        return user_pass
     
def _check_password(passwrod) -> bool:
    """checking if password is atleast 4 charectors long
    
    returns boolian"""
    if len(list(passwrod)) < 4:
        return False
    return True

def hash_password(password) -> str:
       """this is a function for getting password as input and then hashes it using hashlib 
       
        gets password

       returns string"""
       encode_password = password.encode('utf-8')
       hash_object = hashlib.sha256(encode_password)
       hex_dig = hash_object.hexdigest()
       return hex_dig