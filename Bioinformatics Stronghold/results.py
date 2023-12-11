from GeneticAnalysis import GeneticAnalysis

print("[1] DNA: counting DNA nucleotides")
file = open("C:\\Users\\Carolina\\Downloads\\rosalind_dna.txt", "r")
data_rosalind = file.read()
dna_analysed = GeneticAnalysis(data_rosalind)

print(dna_analysed.count_nuc_frequency())

file.close()

print("[2] RNA: transcribing DNA to RNA")
file2 = open("C:\\Users\\Carolina\\Downloads\\rosalind_rna.txt", "r")
data_rosalind2 = file2.read()
dna_analysed2 = GeneticAnalysis(data_rosalind2)

print(dna_analysed2.transcription())

file2.close()

print("[3] REVC: Complementing a strand of DNA")
file3 = open("C:\\Users\\Carolina\\Downloads\\rosalind_revc.txt", "r")
data_rosalind3 = file3.read()
dna_analysed3 = GeneticAnalysis(data_rosalind3)

print(dna_analysed3.create_complementary_string())

file3.close()
