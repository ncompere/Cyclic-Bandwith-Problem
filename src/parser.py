import numpy as np

# Reads files from the HB113 dataset
def read_data(file):
    edges = []
    with open(file, 'r') as file:
        lines = file.readlines()
        first_line = lines[1].split()
        i = 0
        for line in lines[2:]:
            edge = line.split()
            arrete = (int(edge[0]), int(edge[1]))
            edges.insert(i, arrete)
            i += 1
        return int(first_line[0]), int(first_line[1]), edges

