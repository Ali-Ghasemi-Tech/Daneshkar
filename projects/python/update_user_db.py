import json
def update(account , prev_account = None):
    with open("db/users.json" , 'r') as file:
        data = json.load(file)
        file.close

    if account["permission"] == "user":
        if len(data["users"]) == 0: 
            data["users"][account["user_id"]] = account
            with open("db/users.json" , 'w') as file:
                json.dump(data , file , indent=4 ,default=str)
                file.close()
            return
        else:
            
            for i in data["users"]:
                if data["users"][i]["user_name"] == prev_account:
                    data["users"][i] = account
                    with open("db/users.json" , 'w') as file:
                        json.dump(data , file , indent=4 ,default=str)
                    return
                    
        
            
            data["users"][account["user_id"]] = account
            with open("db/users.json" , 'w') as file:
                json.dump(data , file , indent=4 ,default=str)
                file.close()
            return
        

    elif account["permission"] == "admin":
            if len(data["admins"]) == 0: 
                data["admins"][account["admin_id"]] = account
                with open("db/users.json" , 'w') as file:
                    json.dump(data , file , indent=4 ,default=str)
                    file.close()
                return
            else:
            
                for i in data["admins"]:
                    if data["admins"][i]["admin_name"] == prev_account:
                        data["admins"][i] = account
                        with open("db/users.json" , 'w') as file:
                            json.dump(data , file , indent=4 ,default=str)
                        return
                        
            
                
                data["admins"][account["admin_id"]] = account
                with open("db/users.json" , 'w') as file:
                    json.dump(data , file , indent=4 ,default=str)
                    file.close()
                return



    
