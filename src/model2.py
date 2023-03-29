from pycsp3 import *

n, m, edges = data

k = int(sys.argv[1])

# Cyclic bandwith problem

x = VarArray(size=n, dom=range(0, n))

table = {(i, j) for i in range(n) for j in range(n) if min(abs(i-j), n - abs(i-j)) <= k and i != j}

satisfy(AllDifferent(x), [(x[u-1], x[v-1]) in table for u, v in edges])
