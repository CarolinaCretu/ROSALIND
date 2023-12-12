from toolkit import *


class GeneticAnalysis:

    def __init__(self, seq):
        self.seq = seq

    def count_nuc_frequency(self):
        """
        The function counts the frequency of each type of nucleotide
        """
        freq = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        for i in self.seq:
            freq[i] += 1
        return freq

    def create_complementary_string(self):
        """
        The function creates the complementary string
        """
        not_inverse = ''.join([complementary_nucleotides[nuc] for nuc in self.seq])
        return not_inverse[::-1]

    def transcription(self):
        """
        The function creates the respective primary mRNA transcript
        """
        return self.seq.replace("T", "U")

    # # TODO: REDO
    # def cg_count_frequency(self):
    #     """
    #     The function counts the highest content of GC
    #     """
    #     calculation_frequency = round(((self.seq.count("C")) + self.seq.count("G")) / len(self.seq) * 100, 6)
    #     result_dict = {key: calculation_frequency(value) for (key, value) in self.seq.items()}
    #     max_gc_key = max(calculation_frequency, key=result_dict.get)
    #     return f"{max_gc_key[1:]}\n{result_dict[max_gc_key]}"

    def count_kmer(self, kmer):
        """
        The function counts the number of a known kmer
        """
        kmer_count = 0
        for position in range(len(self.seq) - 1):
            if self.seq[position:position + len(kmer)] == kmer:
                kmer_count += 1
        return kmer_count
