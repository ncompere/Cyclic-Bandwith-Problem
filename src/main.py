import parser, model1

def main():
    nb_vertex, nb_edges, edges = parser.read_data(file='HB113/494_bus.mtx.rnd')
    model1.model1(nb_vertex, edges)
    

if __name__ == '__main__':
    main()
