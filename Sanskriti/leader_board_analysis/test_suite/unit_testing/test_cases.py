import unittest
import pytest
from test_suite.unit_testing.test_create_graph_individual import testing_create_graph_individual


class test_create_graph_individual(unittest.TestCase):
    def test_for_int(self):
        with self.assertLogs() as captured:
            testing_create_graph_individual(25)
        self.assertEqual(len(captured.records), 1)
        self.assertEqual(captured.records[0].getMessage(), "Creating graph successful")

    def test_for_float(self):
        with self.assertLogs() as captured:
            testing_create_graph_individual(2.4)
        self.assertEqual(len(captured.records), 1)
        self.assertEqual(captured.records[0].getMessage(),"ID non-existing check")

    def test_for_double(self):
        with self.assertLogs() as captured:
            testing_create_graph_individual(2.4345)
        self.assertEqual(len(captured.records), 1)
        self.assertEqual(captured.records[0].getMessage(),"ID non-existing check")

    def test_for_string(self):
        with self.assertLogs() as captured:
            testing_create_graph_individual("some")
        self.assertEqual(len(captured.records), 1)
        self.assertEqual(captured.records[0].getMessage(),"ID non-existing check")

    def test_for_special_character(self):
        with self.assertLogs() as captured:
            testing_create_graph_individual("&$&&")
        self.assertEqual(len(captured.records), 1)
        self.assertEqual(captured.records[0].getMessage(),"ID non-existing check")


    def test_for_zero_individual_contribution(self):
        with self.assertLogs() as captured:
            testing_create_graph_individual(484)
        self.assertEqual(len(captured.records), 1)
        self.assertEqual(captured.records[0].getMessage(),"contribution check")


if __name__ == '__main__':
    unittest.main()
