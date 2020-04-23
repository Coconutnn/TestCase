import unittest

from src0408 import testBaidu1, testBaidu2


def createsuite():
        # suite = unittest.TestSuite()
        # suite.addTest(unittest.makeSuite(testBaidu1.Baidu1))
        # suite.addTest(unittest.makeSuite(testBaidu2.Baidu2))
        # return suite
        suite1 = unittest.TestLoader().loadTestsFromTestCase(testBaidu1.Baidu1)
        suite2 = unittest.TestLoader().loadTestsFromTestCase(testBaidu2.Baidu2)
        suite = unittest.TestSuite([suite1,suite2])
        return suite
if __name__=="__main__":
        suite = createsuite()
        runner = unittest.TextTestRunner()
        runner.run(suite)