import unittest

import forbidden_integers_analysis

class ForbiddenIntegerTests(unittest.TestCase):

    def test_check_two_ranges_case1(self):
        result = forbidden_integers_analysis.check_two_ranges([0,2],[4,7])
        self.assertIsNotNone(result[1])

    def test_check_two_ranges_case2(self):
        result = forbidden_integers_analysis.check_two_ranges([4,7],[5,8])
        self.assertIsNone(result[1])

    def test_forbidden_integers_stats(self):
        smallest, total = forbidden_integers_analysis.analyze_forbidden_integers(range_min=0,
                                                                        range_max=9,
                                                                        forbidden_lists=[[5,8],[0,2],[4,7]])
        self.assertEqual(3,smallest)
        self.assertEqual(2,total)

if __name__ == '__main__':
    unittest.main()
