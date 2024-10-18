import argparse
from modules.clear import clear
import user_dashboard
import admin_dashboard



parser = argparse.ArgumentParser(description="add new movie as admin")
parser.add_argument("--admin" ,  help="welcome to admin dashboard print" , action="store_true")
parser.add_argument("--password" , help="enter password (ostad the password is daneshkar)")
args = parser.parse_args()

if args.admin and args.password == "daneshkar":
    clear()
    admin_dashboard.run()
elif args.admin and not args.password:
    print("if you want to enter the admin panel you should enter a password as well with --password <set password>")
elif args.admin and args.password != "daneshkar":
    print("the password you have entered is wrong")
else:
    clear()
    user_dashboard.run()
    