def read_FASTA(path):
    file = open(path, "r")
    fasta_dict = {}
    fasta_label = ""
    for line in file.readlines():
        if line[0] == ">":
            fasta_label = line[1:].rstrip("\n")
            fasta_dict[fasta_label] = ""
        else:
            fasta_dict[fasta_label] += line.rstrip("\n")
    return fasta_dict


def gc_count(seq):
    count = 0
    for i in seq:
        if i == "G" or i == "C":
            count += 1
    return round(count * 100 / len(seq), 6)


seq_rosalind = read_FASTA("C:\\Users\\Carolina\\Downloads\\rosalind_gc (2).txt")

for k in seq_rosalind:
    print(f"{k}\n{gc_count(seq_rosalind[k])}")
