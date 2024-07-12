import pytest
from logfile import logClass

def test_Sum():
    assert 2+2 == 4

def testDivision():
    assert 12/3 == 4

def testPrint(setup):   # here inherit setup fun from conftest.py file
    print("Testing..... complete")

# Create/make your log 
class Test_temp(logClass):
    def testPrintLog(self):
        log = self.getLogs()
        log.info("this is my first test case logger info.")
        log.info("test case is starting.....")
        if "jay" in 'jayVaghela':
            assert True
            log.info("test case pass")
        else:
            log.error("test case fail")
            assert False