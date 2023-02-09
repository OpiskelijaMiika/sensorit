import sys            #needed for setting command line
import sensors_main
import unittest
from unittest.mock import patch #neede for integration test

# Unit tests implemented with Python's built-in unittest
# need to be classes, so here we use TestSensors class
# for the tests.
class TestSensors(unittest.TestCase):

    ################### integration TEST##########################

    # The test case test_check_limits1 that tests the check_limits
    # with correct inputs (lower limit 18 and higher limit 22) and
    # expects the method to return True, since the limits are
    # correct.
    def test_check_limits1(self):
        limits = [22, 18]
        result = sensors_main.check_limits(limits)
        self.assertTrue(result)
    """
    def test_check_limits2(self):
        limits = [12, 6]
        result = sensors_main.check_limits(limits)
        self.assertTrue(result, True)

    def test_check_limits3(self):
        limits = [2, 2]
        result = sensors_main.check_limits(limits)
        self.assertTrue(result, True)

    def test_check_limits4(self):
        limits = [-4, -2]
        result = sensors_main.check_limits(limits)
        self.assertTrue(result, True)
    """
        
    # The test case test_check_limits2 that tests the check_limits
    # with incorrect inputs (lower limit 22 and higher limit 18) and
    # expects the method to return False, since the limits are
    # incorrect. To be implemented.

    # Placeholder for the test case test_check_limits3. To be designed
    # and implemented. 

    ################### integration TEST######################

    #Redirect console output to sys.stdout in order
    # to chech its content from the test case
    @patch('builtins.print')
    def test_check_limits1_integration1(self, mock_print):
        # set command line parameters for the test case
        sys.argv = [["sensors_main.py"], [22], [18]]

        # call main from sensors_main
        sensors_main.main()

        # check that the console output is expected error message
        mock_print.assert_called_with("Error: Incorrect command line arguments.")

if __name__ == '__main__':
    unittest.main()