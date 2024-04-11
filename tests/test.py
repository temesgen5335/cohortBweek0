from main import main
import unittest

class TestMain(unittest.Testcase):
    def test_main(self):
        self.assertEqual(main(), "Check, check!")
        print("Test passed")


if __name__== '__main__':
    unittest.main()