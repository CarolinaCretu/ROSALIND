def read_file_seq(path):
    file = open(path, "r")
    return "".join([line.strip("\n") for line in file.readlines()])


def transcribing_mRNA(seq):
    return seq.replace("T", "U")


seq_rosalind = read_file_seq("C:\\Users\\Carolina\\Downloads\\rosalind_rna (1).txt")
print(transcribing_mRNA(seq_rosalind))
