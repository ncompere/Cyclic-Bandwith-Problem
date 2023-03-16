from pycsp3 import *

# Cyclic bandwith problem model with integer finite domain variables

n, m, edges = data

x = VarArray(size=n, dom=range(1, n+1))

satisfy(
    AllDifferent(x)
)
minimize(
    Maximum(min(abs(x[i] - x[j]), n - abs(x[i] - x[j])) for i, j in edges)
)