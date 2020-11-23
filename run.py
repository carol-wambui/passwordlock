#!User/bin/ev/python3
from user import Credentials , User
def demand_user(username,password):
    createuser = User(username,password)
    return createuser

def enter_user (username,password):
   save_user = User.user_recognised(username,password)
   return save_user

def save_user(user):
    user.save_user()

def user_credentials(account_name,user_name,password):
    new_credentials = Credentials(account_name,user_name,password)
    return new_credentials

def save_credentials(credentials):
    credentials.save_credentials()

def delete_credentials(credentials):
    credentials.delete_credentials()

def view_credentials():
    return Credentials.view_credatials()

def credatials_user_exists(account_name):
    return credentials.credatials_user_exists(account_name)

def find_account(account_name):
    return Credentials.view_account_name(account_name)

def bring_password ():
    bring_password =Credentials.bring_password()
    return bring_password
    
