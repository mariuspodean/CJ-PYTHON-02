import unittest
import sys
from final_project.final_project_rusu_daniel import application

class TestDatabase(unittest.TestCase):
    def test_database_object_attribute_initialize(self):
        acc_name='username'
        acc_pass='password'

        test_database=application.Database(acc_name,acc_pass)

        assert hasattr(test_database,'acc_name'), 'Database class is missing acc_name attribute'
        assert hasattr(test_database,'acc_pass'), 'Database class is missing acc_pass attribute'

class TestUsers(unittest.TestCase):
    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")


    @unittest.skipUnless(sys.platform.startswith("Lin"), "requires Linux")
    def test_linux_support(self):
         pass

if __name__ == '__main__':
    unittest.main()

        

