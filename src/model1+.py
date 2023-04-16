import re
import sys
from pycsp3 import *

n, m, edges = data

x = VarArray(size=n, dom=range(n))

satisfy(
    x[0] == 1,
    x[2] < x[n-1],
    AllDifferent(x)
)

minimize(
   Maximum(Minimum(abs(x[u] - x[v]), n - abs(x[u] - x[v])) for u, v in edges)
)
