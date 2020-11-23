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
    
def main():
    while True:
        print('welcome to passwordlock use this command AB to login,CD  to create account, EF to signin, GH to exit')
        enter = input().lower()
        if enter =='ab':
            print('login')
            username = input('enter username')
            
            print('use z to create password,n to auto generate password,s to exit')
            password = input().lower()

            if password == 'z':
                password = input('enter password')

            elif password == 'n':
                password=bring_password()

            else:
                print('invalid input')
                
            save_user(demand_user(username,password))
            print(f"welcome {username}, your account password is {password} use it to login")



        elif enter == 'cd':
            print("enter your password to signin")
            print("input your username")
            username = input()
            print("input your password")
            password = input()
            Real_user = enter_user(username,password)
            if Real_user == username:
                print(f"Hi {username}")
                while True:
                    print("use j to create credentials,del to Delete,cw to display,wm to find credentials, x exit")
                    create_credentials = input().lower()
                    if create_credentials =='j':
                        print("create ccreate_credentialsredentials")
                        print("enter account_name")
                        account_name= input()
                        print("enter username")
                        username = input()
                        print('use z to create password,n to auto generate password,s to exit')
                        password = input().lower()

                        if password == 'z':
                            password = input('enter password: ')

                        elif password == 'n':
                              password = bring_password()

                        else:
                            print('invalid input')

                        save_credentials(user_credentials(account_name,username,password))
                        print(f"your credentials are {account_name},{username},{password} has been created")

                            
                    elif create_credentials == "del":
                        print("enetr account to delete")
                        account = input()
                        if find_account(account):
                            account_to_delete = find_account(account)
                            account_to_delete.delete_credentials()
                            print("account deleted")
                        else:
                            print("we did not found account without name")

                    elif create_credentials=="cw":
                        print("your credentials are here")
                        if view_credentials():
                            for account in view_credentials():
                                print(f"account: {account_name} \n username: {username} \n password: {password} \n")
                        
                        else:
                            print(" no credentials" )
                    elif create_credentials == "wm":
                        print("enter account to search")
                        account = input()
                        if find_account(account):
                            search = find_account(account)
                            print(f"account: {search.account_name} \n username:{search.user_name} \n password: {search.password} \n")
                        else:
                            print("The credentials does not exist")

                    else:
                        print("exit")

        else:
            print("good day!")




if __name__ == "__main__":
    main()