from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from searchtests import searchtests
from assertionstest import AssertionsTest

assertions_test = TestLoader().loadTestsFromTestCase(assertions_test)
search_test = TestLoader().loadTestsFromTestCase(searchtests)

smoke_test = TestSuite([assertions_test, searchtest])

kwargs = {
    "output": 'smoke-report'
}

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)