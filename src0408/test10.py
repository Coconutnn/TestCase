import unittest

from src0408 import testBaidu1, testBaidu2


def createsuite():
    suite = unittest.TestSuite()
    suite.addTest(testBaidu1.Baidu1("test_baidusearch"))
    suite.addTest(testBaidu1.Baidu1("test_hao"))
    suite.addTest(testBaidu2.Baidu2("test_baidusearch"))
    return suite

if __name__=="__main__":
    suite = createsuite()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)