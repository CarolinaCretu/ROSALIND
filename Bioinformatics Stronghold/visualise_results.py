from GeneticAnalysis import GeneticAnalysis
from toolkit import *


def cg_count_frequency(seq):
    """
    The function counts the highest content of GC
    """
    return round(((seq.count("C")) + seq.count("G")) / len(seq) * 100, 6)


print("\n[1] DNA: counting DNA nucleotides")
data_rosalind = readFileSimple("C:\\Users\\Carolina\\Downloads\\rosalind_dna.txt")
dna_analysed = GeneticAnalysis(data_rosalind).count_nuc_frequency()
result_reformatted = " ".join([str(val) for key, val in dna_analysed.items()])
print(result_reformatted)

print("\n[2] RNA: transcribing DNA to RNA")
data_rosalind2 = readFileSimple("C:\\Users\\Carolina\\Downloads\\rosalind_rna.txt")
print(GeneticAnalysis(data_rosalind2).transcription())

print("\n[3] REVC: Complementing a strand of DNA")
data_rosalind3 = readFileSimple("C:\\Users\\Carolina\\Downloads\\rosalind_revc.txt")
print(GeneticAnalysis(data_rosalind3).create_complementary_string())

print("\n[4] FIB: Rabbits and Recurrence Relations")

# TODO: make it a function in the class
print("\n[5] GC: Computing GC Content")
fasta_rosalid = readFastaFile(readFileReformat("C:\\Users\\Carolina\\Downloads\\rosalind_gc (1).txt"))
result_dict = {key: cg_count_frequency(value) for (key, value) in fasta_rosalid.items()}
max_gc_key = max(result_dict, key=result_dict.get)
print(fasta_rosalid)
print(result_dict)
print(f"{max_gc_key[1:]}\n{result_dict[max_gc_key]}")


