from pycsp3 import *

# Cyclic bandwith problem model with integer finite domain variables

n, m, edges = data

x = VarArray(size=n, dom=range(n))

satisfy(
    AllDifferent(x)
)
minimize(
    Maximum(min(abs(x[i-1] - x[j-1]), n - abs(x[i-1] - x[j-1]))
            for [i, j] in edges)
)
