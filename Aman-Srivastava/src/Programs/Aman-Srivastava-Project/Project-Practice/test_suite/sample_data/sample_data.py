import unittest
from test_suite.unit.test_data_extraction import Testing_Plot_Class


class Test_Class(unittest.TestCase):

    def test_for_int(self):
        with self.assertLogs() as captured:
            Testing_Plot_Class(25)
        self.assertEqual(len(captured.records), 1)
        self.assertEqual(captured.records[0].getMessage(), "Plot Successful")

    def test_for_zero_contribution(self):
        with self.assertLogs() as captured:
            Testing_Plot_Class(484)
        self.assertEqual(len(captured.records), 1)
        self.assertEqual(captured.records[0].getMessage(), "Zero Contribution Check")

    def test_for_double(self):
        with self.assertLogs() as captured:
            Testing_Plot_Class(45.3365859965333)
        self.assertEqual(len(captured.records), 1)
        self.assertEqual(captured.records[0].getMessage(), "Non Existing Check")

    def test_for_float(self):
        with self.assertLogs() as captured:
            Testing_Plot_Class(2.7)
        self.assertEqual(len(captured.records), 1)
        self.assertEqual(captured.records[0].getMessage(), "Non Existing Check")

    def test_for_string(self):
        with self.assertLogs() as captured:
            Testing_Plot_Class("UserName")
        self.assertEqual(len(captured.records), 1)
        self.assertEqual(captured.records[0].getMessage(), "Non Existing Check")

    def test_for_negative(self):
        with self.assertLogs() as captured:
            Testing_Plot_Class(-8)
        self.assertEqual(len(captured.records), 1)
        self.assertEqual(captured.records[0].getMessage(), "Non Existing Check")

    def test_for_symbols(self):
        with self.assertLogs() as captured:
            Testing_Plot_Class("%$=-=")
        self.assertEqual(len(captured.records), 1)
        self.assertEqual(captured.records[0].getMessage(), "Non Existing Check")


if __name__ == '__main__':
    unittest.main()
