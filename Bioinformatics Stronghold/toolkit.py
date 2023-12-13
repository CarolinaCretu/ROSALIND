# functions for working with files


def readFileSimple(file_path):
    """
    Read a simple txt file
    """
    with open(file_path, "r") as f:
        return f.readline().rstrip("\n")


def readFileReformat(file_path):
    """
    Reads the file and returns a list of lines
    """
    with open(file_path, "r") as f:
        return [i.strip() for i in f.readlines()]


def readFastaFile(fasta_path):
    """
        Reads Fasta file
        """
    fasta_dict = {}  # dictionary for labels + data
    fasta_label = ""  # string for holding the current label
    for line in fasta_path:
        if ">" in line:
            fasta_label = line
            fasta_dict[fasta_label] = ""
        else:
            fasta_dict[fasta_label] += line
    return fasta_dict


# other biological info needed

nucleotides = ['A', 'C', 'G', 'T']
complementary_nucleotides = {"A": "T", "C": "G", "G": "C", "T": "A"}