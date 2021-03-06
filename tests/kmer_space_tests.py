import unittest

from kmer_space import KMerSpace
from tests.utils import is_kmer_list_sorted

common_alphabet = ["A", "C", "T", "G"]


class KMerSpaceTest(unittest.TestCase):

    def test_initialization(self):
        kmer_space = KMerSpace(k=4, alphabet=common_alphabet)
        self.assertEqual(len(kmer_space.get_sorted_by_kmer()), 136)

    def test_adding_kmer(self):
        kmer_space = KMerSpace(k=4, alphabet=common_alphabet)
        kmer = "ACTG"
        kmer_space.increase(kmer)
        self.assertEqual(kmer_space.get_value(kmer), 1)

    def test_is_output_kmer_list_is_sorted_by_kmer(self):
        kmer_space = KMerSpace(k=4, alphabet=common_alphabet)
        res = kmer_space.get_sorted_by_kmer()
        self.assertTrue(is_kmer_list_sorted(res))

