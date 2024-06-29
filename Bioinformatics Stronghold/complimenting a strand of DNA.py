complimentary_nuc = {"A": "T", "C": "G", "G": "C", "T": "A"}


def read_file_seq(path):
    file = open(path, "r")
    return "".join([line.strip("\n") for line in file.readlines()])


def compliment(seq):
    compliment_no_rev = ""
    for i in seq:
        compliment_no_rev += complimentary_nuc[i]
    return compliment_no_rev[::-1]


seq_rosalind = read_file_seq("C:\\Users\\Carolina\\Downloads\\rosalind_revc (1).txt")
print(compliment(seq_rosalind))

