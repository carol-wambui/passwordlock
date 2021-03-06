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

    @classmethod
    def view_account_name(cls,account_name):
        for credentials in cls.user_credentials:
            if credentials.account_name == account_name:
                return credentials

    @classmethod
    def view_credatials(cls):
        return cls.user_credentials

    def bring_password (stringcashy=8):
        password =string.ascii_uppercase +string.ascii_lowercase +string.digits + "(/|~!.@,)#{?&[%]^}&*"
        return "".join(random.choice(password)for i in range(stringcashy))

    

