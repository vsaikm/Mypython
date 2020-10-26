import unittest
import main

class TestMain(unittest.TestCase):
    def setUp(self):
        print('about to test a function')
        
    def test_do_stuff(self):
        testparam = 10
        result = main.do_stuff(testparam)
        self.assertEqual(result,15)

    #def test_do_stuff2(self):
    #    testparam = 'hsjgfhhfjbg'
    #    result = main.do_stuff(testparam)
     #   self.assertIsInstance(result,ValueError)


   # def test_do_stuff3(self):
    #    testparam = None
    #    result = main.do_stuff(testparam)
     #   self.assertEqual(result,AssertionError)


if __name__ == '__main__':
    unittest.main()
                
