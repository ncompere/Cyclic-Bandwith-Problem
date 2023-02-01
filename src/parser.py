import numpy as np


def read_data(file):
    edges = []
    with open(file, 'r') as file:
        lines = file.readlines()
        first_line = lines[1].split()
        for line in lines[2:]:
            edge = line.split()
            arrete = (int(edge[0]), int(edge[1]))
            edges = np.append(edges, arrete)
        return int(first_line[0]), int(first_line[1]), edges


nb_vertex, nb_edges, edges = read_data(file='HB113-20230131/494_bus.mtx.rnd')

print(edges)
