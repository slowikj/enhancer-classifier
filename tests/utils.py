def is_kmer_list_sorted(res):
    return all(res[i][0] < res[i + 1][0] for i in range(len(res) - 1))
