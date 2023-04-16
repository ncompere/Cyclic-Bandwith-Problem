import sys
import os
import re
from os.path import isfile, join, exists
from subprocess import check_output, DEVNULL, CalledProcessError
import signal
from time import time, sleep
import json
import parser
from math import ceil, floor
from random import randint, choice
import string as st


def run_solver(filename, k, lower_bound, upper_bound, model, timeout, path="../data/"):
    output = ''.join(choice(st.ascii_uppercase + st.digits) for _ in range(10))
    output = "solver_" + output + ".xml"
    if model == "model1" or model == "model2" or model == "model1+" or model == "model2+":
        genXML = f"python3 {model}.py {k} -data={path+filename} -output={output} -solve"
        try:
            _ = check_output(genXML.split(), stderr=DEVNULL).decode(sys.stdout.encoding)
        except CalledProcessError as error:
            print(filename, str(error))
        cmd = f"java -jar ACE.jar {output} -t={timeout} -lb={lower_bound} -ub={upper_bound}"
        try:
            output = check_output(cmd.split(), stderr=DEVNULL).decode(sys.stdout.encoding)
        except CalledProcessError as error:
            print(filename, str(error))
    else:
        pass
    solution = True
    lines = output.splitlines()
    print(lines)
    for line in lines:
        if model == "model1" or model == "model2" or model == "model1+" or model == "model2+":
            solutionUNS = re.compile("s UNSATISFIABLE")
            solutionUNK = re.compile("s UNKNOWN")
            if solutionUNS.search(line) or solutionUNK.search(line):
                solution = False
                break
        else:
            if "$" in line:
                solution = eval(line.split("$")[1].split()[0])
    return solution


def dichotomie(filename, lower_bound, upper_bound, model, timeout):
    if lower_bound < upper_bound:
        temp_k = int((lower_bound + upper_bound) / 2)
        has_solution = run_solver(filename, temp_k, lower_bound, upper_bound, model, timeout)
        if temp_k > 0 and has_solution:
            return dichotomie(filename, lower_bound, temp_k-1, model, timeout)
        else:
            return dichotomie(filename, temp_k+1, upper_bound, model, timeout)
    else:
        return upper_bound


def run_dicho_solver(file, model, timeout, path="../data/"):
    filename = path + file
    elapsed_time = time()
    with open(filename, 'r') as f:
        graph_data = json.load(f)
        num_vertices = graph_data['V']
    maxdegree = parser.calculate_max_degree(file)
    lower_bound = ceil(maxdegree/2)
    upper_bound = floor(num_vertices/2)

    k = dichotomie(file, lower_bound, upper_bound, model, timeout)

    elapsed_time = time() - elapsed_time

    if k > 0:
        print(f"Solved {file} in {elapsed_time:.2f} seconds with k = {k}")
    else:
        print(f"Could not solve {file} in {elapsed_time:.2f} seconds")

    fnames = [f for f in os.listdir(".") if f.startswith("solver_")]
    for fname in fnames:
        os.remove(fname)

    