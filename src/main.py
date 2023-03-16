# from pycsp3 import *
import parser
# import model
import sys


def main(argv):
    print(sys.argv[1])
    parser.read_data_v2(file=sys.argv[1])


if __name__ == '__main__':
    main(sys.argv[0:])

# Exécuter en ligne de commande
# Voir les options d'affichages de PyCSP3
