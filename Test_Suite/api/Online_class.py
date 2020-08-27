import unittest
from testcase import test_wenwo_api, test_online_class


def get_suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    # suite.addTests(loader.loadTestsFromTestCase(test_wenwo_api.TestCasewenwo))
    # suite.addTests(loader.loadTestsFromTestCase(test_wenwo_api.Testpatsplitsub))
    # suite.addTests(loader.loadTestsFromTestCase(test_wenwo_api.TestdoctorClass))
    # suite.addTests(loader.loadTestsFromTestCase(test_online_class.TestdoctorClass))
    suite.addTests(loader.loadTestsFromTestCase(test_wenwo_api.Data_other))
    return suite
