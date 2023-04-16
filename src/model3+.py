import io
import os
import re
import sys
import json
import gzip
import shutil
import os.path
import string as mS
import random as mR
import numpy as np
from time import time

k = int(sys.argv[1])
datapath = "../data/" + sys.argv[2]
cons1 = 1
outpath = ''.join(mR.choice(mS.ascii_uppercase + mS.digits) for _ in range(24))
outpath += ".cnf"
solve = True
wr = True

elapsedT = time()

with open(datapath) as f:
    data = json.load(f)

n, m, edges = data.values()
del(data)

# Clause 1

T = n**2+1
buff = io.StringIO()
out = open(outpath, "w")
def flushToFile(f, s, i, maxiter):
    if i > maxiter:
        s.seek(0)
        shutil.copyfileobj(s, f)
        s = io.StringIO()
        i = 0
    return s, i

niter = 1
maxiter = 10000
buff.write(f"{T} 0\n")
buff.write(f"{cons1} 0\n")
numclauses = 1

# Clauses 2 et 3

for i in range(n):
    c2 = []
    for j in range(n):
        c3 = [-(n*i+j)-1]
        for k in range(n):
            if k != j:
                c3.append(-(n*k+i)-1)
        c2.append(n*i+j+1)
        c3.append(0)
        buff, niter = flushToFile(out, buff, niter, maxiter)
        buff.write(" ".join([str(item) for item in c3]) + "\n")
        niter += 2
        numclauses += 2
    c2.append(0)
    buff, niter = flushToFile(out, buff, niter, maxiter)
    buff.write(" ".join([str(item) for item in c2]) + "\n")
    niter += 1
    numclauses += 1

P = np.full((n, n), False)
for i in range(n):
    for j in range(n):
        if min(abs(j - i), n - abs(j - i)) <= k:
            P[i][j] = True

# Clause 4

for (u, v) in edges:
    for i in range(n):
        for j in range(n):
            if P[i][j]:
                buff, niter = flushToFile(out, buff, niter, maxiter)
                buff.write(f"{-(n*u+i)-1} {-(n*v+j)-1} {T} 0\n")
                niter += 1
                numclauses += 1
            else:
                buff, niter = flushToFile(out, buff, niter, maxiter)
                buff.write(f"{-(n*u+i)-1} {-(n*v+j)-1} {-T} 0\n")
                niter += 1
                numclauses += 1

del(P)

instance = datapath.split("/")[-1].split(".")[0]

content = buff.getvalue()
buff.close()
if content != "":
    out.write(content)
out.close()

with open(outpath, "r") as readOut:
    with gzip.open(outpath+".gz", "w") as out:
        out.write(f"c {instance}\n".encode())
        out.write(f"p cnf {T} {numclauses}\n".encode())
        out.write(readOut.read().encode())
os.remove(outpath)

elapsedT = time() - elapsedT

print(f"* Generated the file {outpath} in \033[1;32m{elapsedT:.2f}\u001B[0m seconds.")

if solve:
    from pysat.formula import CNF
    from pysat.solvers import Glucose4

    result = None
    elapsedT = time()
    ins = CNF()
    ins.from_file(outpath+".gz", compressed_with="gzip")

    with Glucose4(ins.clauses) as s:
        result = s.solve()
    elapsedT = time()-elapsedT

    if wr:
        print(f"  $ {result}")
    print(f"  * Solved {outpath} in \033[1;32m{elapsedT:.2f}\u001B[0m seconds.")
