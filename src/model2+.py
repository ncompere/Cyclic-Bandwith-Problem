import re
import sys
from pycsp3 import *

k = int(sys.argv[1])

n, m, edges = data

x = VarArray(size=n, dom=range(n))

table = {(i, j) for i in range(n) for j in range(n)
                if min(abs(i - j), n - abs(i - j)) <= k
                   and i != j}

satisfy(
    x[0] == 1,
    x[2] < x[n-1],
    AllDifferent(x),
    [(x[u], x[v]) in table for u, v in edges]
)
