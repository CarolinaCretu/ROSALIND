output_file = []

with open("C:\PYTHON\phyton_projects\ROSALIND\ROSALIND\Python Village\imput_file", "r") as f:
    for line in f:
        line = line.strip()  # strip removes any spaces
        output = output_file.append(line)

output_final = output_file[1::2]

with open("C:\PYTHON\phyton_projects\ROSALIND\ROSALIND\Python Village\imput_file", "w") as f:
    f.write("\n".join([i for i in output_final]))

