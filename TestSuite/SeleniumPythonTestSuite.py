import unittest
#from TestCases.ForgotPassword import Forgot
from HtmlTestRunner import HTMLTestRunner
from TestCases.ForgotPassword import Flipcart1
from TestCases.ProductPlaceOrder import Flipcart

# get all tests from SearchText and HomePageTest class
forgot = unittest.TestLoader().loadTestsFromTestCase(Flipcart1)
placeorder = unittest.TestLoader().loadTestsFromTestCase(Flipcart)

# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([forgot, placeorder])

# open the report file
outfile = open("D:\Selenium-PYTHON\Python-Test-Automation-Framework-master\Reports\SeleniumPythonTestSummary.html", "w")

# configure HTMLTestRunner options
#runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='Test Report', description='Acceptance Tests')

runner=HTMLTestRunner(combine_reports=True, report_name="D:\Selenium-PYTHON\Python-Test-Automation-Framework-master\Reports\ReportsMyReport", add_timestamp=False).run(test_suite )

#runner = HTMLTestRunner(output='D:\Selenium-PYTHON\Python-Test-Automation-Framework-master\Reports\SeleniumPythonTestSummary')

#runner.run(test_suite )
# run the suite
#unittest.TextTestRunner(verbosity=2).run(test_suite)