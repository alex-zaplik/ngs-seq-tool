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

if __name__ == '__main__':
    unittest.main()