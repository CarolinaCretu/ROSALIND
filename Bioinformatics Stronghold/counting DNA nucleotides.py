def read_file_seq(path):
    file = open(path, "r")
    return "".join([line.strip("\n") for line in file.readlines()])


def nucleotides_count(seq):
    nuc = {"A": 0, "C": 0, "G": 0, "T": 0}
    for i in seq:
        nuc[i] += 1
    return nuc


seq_rosalind = read_file_seq("C:\\Users\\Carolina\\Downloads\\rosalind_dna (1).txt")
dict_result_seq = nucleotides_count(seq_rosalind)

print(" ".join([str(values) for keys, values in dict_result_seq.items()]))
