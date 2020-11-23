import random
import string

class User:
    user_list = []

    def __init__(self,user_name, password):
      self. user_name = user_name
      self.password = password
      

    def save_user(self):
          User.user_list.append(self)

    @classmethod
    def user_recognised(cls,user_name,password):
        current_user = ""
        for user in User.user_list:
         if user.user_name == user_name and user.password == password:
            current_user = user.user_name
            return current_user

class Credentials:
    user_credentials = []

    def __init__(self,account_name,user_name,password):
        self. account_name = account_name 
        self.user_name = user_name
        self.password = password

    def save_credentials(self):
          Credentials.user_credentials.append (self)

    def delete_credentials(self):
           Credentials.user_credentials.remove (self)

    @classmethod
    def credentials_user_exists(cls,account_name):
        for credentials in cls.credentials:
            if credentials.account == account:
                return True
        return False 

    
