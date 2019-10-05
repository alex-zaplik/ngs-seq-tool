import unittest
from algorithmChecker import checkAlgorithm


class TestCheckAlgorithm(unittest.TestCase):
    def test_A_valid(self):
        self.assertTrue(checkAlgorithm('A'))

    def test_CT_valid(self):
        self.assertTrue(checkAlgorithm(['C', 'T']))
    
    def test_illumina_example_valid(self):
        self.assertTrue(
            checkAlgorithm(
                ['ATTCAGAA',
                'GAATTCGT',
                'AGCGATAG']
             )
        )
    
    def test_illumina_example_not_valid(self):
        self.assertFalse(
            checkAlgorithm(
                ['GCTACGCT',
                'GTAGAGGA',
                'GGAGCTAC']
            )
        )
    
    # extra data tests

    def test_A_extra_data(self):
        self.assertEqual(checkAlgorithm('A', True), [True])

    def test_CT_extra_data(self):
        self.assertEqual(checkAlgorithm(['C', 'T'], True), [True])
    
    def test_illumina_example_extra_data(self):
        self.assertEqual(
            checkAlgorithm(
                ['ATTCAGAA',
                'GAATTCGT',
                'AGCGATAG'],
                True
             ),
             [True, True, True, True, True, True, True, True]
        )
    
    def test_illumina_example_not_extra_data(self):
        self.assertEqual(
            checkAlgorithm(
                ['GCTACGCT',
                 'GTAGAGGA',
                 'GGAGCTAC'],
                True
            ),
            [False, True, True, True, True, False, True, True]
        )

if __name__ == '__main__':
    unittest.main()