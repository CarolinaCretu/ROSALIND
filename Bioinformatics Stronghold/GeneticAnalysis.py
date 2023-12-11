from toolkit import *
class GeneticAnalysis:

    def __init__(self, seq):
        self.seq = seq

    def count_nuc_frequency(self):
        """
        The function counts the frequency of each type of nucleotide
        """

        return self.seq.count("A"), self.seq.count("G"), self.seq.count("C"), self.seq.count("T")

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

    def count_kmer(self, kmer):
        """
        The function counts the number of a known kmer
        """
        kmer_count = 0
        for position in range(len(self.seq) - 1):
            if self.seq[position:position + len(kmer)] == kmer:
                kmer_count += 1
        return kmer_count
