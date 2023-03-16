import numpy as np
import json
import os

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
        return int(first_line[0]), int(first_line[2]), edges


def read_data_v2(file):
    graph = {}
    with open(file, 'r') as file:
        lines = file.readlines()
        name = lines[0].split(":")[1][1:-9]
        print(name)
        print("Reading instance : " + name)
        size_data = lines[1].split()
        graph["V"] = int(size_data[1])
        graph["E"] = int(size_data[2])
        graph["edges"] = []
        for line in lines[2:]:
            edge = line.split()
            arrete = (int(edge[0]), int(edge[1]))
            graph["edges"].append(arrete)
        print("Done")
    path = "../data"
    file_name = name + ".json"
    complete_name = os.path.join(path, file_name)
    with open(complete_name, "w") as outfile:
        json.dump(graph, outfile)

