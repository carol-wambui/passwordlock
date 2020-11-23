import unittest
from user import, credentials

class Testclass(unittest.Testclass):

    def test_init(self):
        self.assertEqual(self.createuser.username,"instagram")
        self.assertEqual(self.createuser.passwod, "Kapreaty")

    def setUp(self):

        self.new_user = User("instagram","Kapreaty")

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

class Testcredentials(unittest.Testcase):
    def setUp(self):

        self.new_credentials= credentials("account","instagram","Kapreaty")

    def tearDown(self):
        credentials.user_credentials = []

    def test_details(self):
        self.assertEqual(self.new_credentials.account,"account")
        self.assertEqual(self.new_credentials.username,"instagram")
        self.assertEqual(self.new_credentials.passwod,"Kapreaty")

    def text_save_credentials(self):

        self.new_credentials.save_credentials()
        self.assertEqual(len(credentials.user_credentials),1)

    def find_credentials(self):
        self.new_credentials.save_credentials()
        test_credentials = credentials("account","username","password")
        test_credentials.save_credentials()

        the_credentials= credentials.find_account("account")
        self.assertEqual(the_credentials.account,test_credentials.account)

    def text_exist(self):

        self.new_credentials.save_credentials()
        test_credentials = credentials("account","username","password")

        search_credential = credentials .credentials.credentialuser_exist("account")
        self.assertTrue(search_credential)

    def delete_credentials(self):
        self.new_credentials.save_credentials()
        test_credentials = credentials("account","username","password")
        test_credentials.save_credentials()

        self.new_credentials.delete_credentials()
        self.assertEqual(len(credentials.user_credentials),1)

    def test_savemany_account(self):
        self.new_credentials.save_credentials()
        test_credentials = credentials("account","sername","password")
        test_credentials.save_credentials()

        self.assertEqual(len(credentials.user_credentials),2)


if_name_== '_main_':
    unnittest.main()

    