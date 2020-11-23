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

