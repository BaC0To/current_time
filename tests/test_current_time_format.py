import unittest
from datetime import datetime
from time_check import time_format_check


current_time_unformatted = datetime.now() # current date and time
current_time_formatted = current_time_unformatted.strftime("%H:%M:%S.%f") # e.g. --> 10:51:38.211075

class TestTimeFormat(unittest.TestCase):


    def test_if_time_formatted_correctly(self):
        #10:51:38.211075
        test_time = current_time_formatted
        self.assertTrue(time_format_check(test_time))

    def test_if_time_not_formatted_correctly(self):
        #10:51:38
        test_time = "10:51:38"
        self.assertFalse(time_format_check(test_time))


if __name__ == '__main__':
    unittest.main()
