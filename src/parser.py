import numpy as np
import pickle as pk
import json
import os
from os import listdir, makedirs, system
from os.path import isfile, join, exists


# Reads files from the HB113 dataset and writes them in json format
def read_data(file):
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


def read_all_data():
    for file_name in os.listdir("../HB113/"):
        if file_name.endswith(".rnd"):
            print(os.path.join("../HB113/", file_name))
            parser.read_data(file=os.path.join("../HB113/", file_name))


def calculate_max_degree(file, path="../data/"):
    filename = path + file
    with open(filename, 'r') as f:
        graph_data = json.load(f)
        num_vertices = graph_data['V']
        num_edges = graph_data['E']
        edges = graph_data['edges']
        degree = [0] * num_vertices
        for edge in edges:
            degree[edge[0]-1] += 1
            degree[edge[1]-1] += 1
    return max(degree)


# test = calculate_max_degree("curtis54.json")
# print(test)