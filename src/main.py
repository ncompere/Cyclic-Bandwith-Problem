from pycsp3 import *
import parser
import model


def main():
    nb_vertex, nb_edges, edges = parser.read_data(file='HB113/494_bus.mtx.rnd')
    # print(edges[0][0])
    if solve(model.model1(nb_vertex, edges)) is SAT:
        print("x:", x)


if __name__ == '__main__':
    main()
