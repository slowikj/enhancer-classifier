import unittest

from kmer_space import KMerSpace

common_alphabet = ["A", "C", "T", "G"]


class KMerSpaceTest(unittest.TestCase):

    def test_initialization(self):
        kmer_space = KMerSpace(k=4, alphabet=common_alphabet)
        self.assertEqual(len(kmer_space.get_sorted_by_kmer()), 136)

    def test_increase_1_a_key_that_is_explicitly_in_dict(self):
        kmer_space = KMerSpace(k=4, alphabet=common_alphabet)
        kmer = "ACTG"
        kmer_space.increase(kmer)
        self.assertEqual(kmer_space.get_value(kmer), 1)

