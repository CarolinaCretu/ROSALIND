def read_file_seq(path):
    file = open(path, "r")
    return [line.strip("\n")for line in file.readlines()]


def count_point_mutation(seq_list):
    count = 0
    for i in range(len(seq_list[0])):
        if seq_list[0][i] != seq_list[1][i]:
            count += 1
    return count


seq_rosalind = read_file_seq("C:\\Users\Carolina\Downloads\\rosalind_hamm.txt")
print(count_point_mutation(seq_rosalind))

