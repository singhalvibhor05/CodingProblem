"""
Module to test the basic requirement of highest_share
"""
import unittest
from highest_share import get_max_shares_list


class ParseCSVTest(unittest.TestCase):

    def setUp(self):
        self.data = 'test_shares_data.csv'

    def test_get_max_share_list(self):
        status, data = get_max_shares_list(self.data)

        self.assertTrue(status)
        self.assertListEqual(
            data['Company-A'], ['2000', 'Mar', 1000])


if __name__ == '__main__':
    unittest.main()
