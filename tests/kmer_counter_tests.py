import unittest

from kmer_counter import KmerCounter


class MyTestCase(unittest.TestCase):

    def test_seq_of_one_kmer_gives_count_1_only_for_one_entry(self):
        k = 4
        kmer = "ACTA"
        res = KmerCounter(kmer).get_kmer_counts(k)
        self.assertEqual(len(res), 136)
        self.assertEqual(res[kmer], 1)
        self.assertEqual(len(list(filter(lambda x: x == 0, [res[i] for i in res.keys() if i != kmer]))), 135)

    def test_seq_with_2_different_kmers(self):
        k = 4
        kmer = "ACTAA"
        res = KmerCounter(kmer).get_kmer_counts(k)
        self.assertEqual(len(res), 136)
        self.assertEqual(res["ACTA"], 1)
        self.assertEqual(res["CTAA"], 1)

    def test_kmer_frequencies_with_2_different_kmers(self):
        k = 4
        kmer = "ACTAA"
        res = KmerCounter(kmer).get_kmer_frequencies(k)
        self.assertEqual(len(res), 136)
        self.assertEqual(res["ACTA"], 1/len(kmer))
        self.assertEqual(res["CTAA"], 1/len(kmer))

    def test_kmer_frequencies_sorted_list(self):
        k = 4
        kmer = "ACTAA"
        res = KmerCounter(kmer).get_kmer_frequencies_sorted_list(k)
        self.assertEqual(len(res), 136)
        self.assertTrue(all(res[i][0] < res[i+1][0] for i in range(len(res) - 1)))  # check if sorted


if __name__ == '__main__':
    unittest.main()
