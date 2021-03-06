import unittest
from User import credentials

class TestCredentials(unittest.TestCase):
    def setUp(self):
        '''
        test to confirm if default account exist
        '''

        self.new_credentials= credentials("account","instagram","Kapreaty")

    def test_details(self):
        '''
        test to confirm if new credentials can be added
        '''

        self.assertEqual(self.new_credentials.account,"account")
        self.assertEqual(self.new_credentials.username,"instagram")
        self.assertEqual(self.new_credentials.passwod,"Kapreaty")

    def test_init(self):
        '''
        test to confirm if username or password are there
        '''
        self.assertEqual(self.createuser.username,"instagram")
        self.assertEqual(self.createuser.passwod, "Kapreaty")

    def setUp(self):
        '''
        test to confirm if a new user can be added
        '''
        self.new_user = User("instagram","Kapreaty")

    def test_save_user(self):
        
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

    def tearDown(self):
        credentials.user_credentials = []


    def text_save_credentials(self):
        '''
        test to confirm if credential is saved
        '''

        self.new_credentials.save_credentials()
        self.assertEqual(len(credentials.user_credentials),1)

    def find_credentials(self):
        '''
        test to confirm if users can search for their credentials
        '''
        self.new_credentials.save_credentials()
        test_credentials = credentials("account","username","password")
        test_credentials.save_credentials()

        the_credentials= credentials.find_account("account")
        self.assertEqual(the_credentials.account,test_credentials.account)

    def text_exist(self):
        '''
        test to confirm if user can search credentials
        '''

        self.new_credentials.save_credentials()
        test_credentials = credentials("account","username","password")

        search_credential = credentials .credentials.credentialuser_exist("account")
        self.assertTrue(search_credential)

    def delete_credentials(self):
        '''
        test to cornfirm if user can delete saved credentials
        '''
        self.new_credentials.save_credentials()
        test_credentials = credentials("account","username","password")
        test_credentials.save_credentials()

        self.new_credentials.delete_credentials()
        self.assertEqual(len(credentials.user_credentials),1)

    def test_save_credentials(self):
        '''
        test to confirm if saved credentials exist
        '''
        self.new_credentials.save_credentials()
        test_credentials = credentials("account","sername","password")
        test_credentials.save_credentials()

        self.assertEqual(len(credentials.user_credentials),2)


if_name_== '_main_':
    unnittest.main()

    