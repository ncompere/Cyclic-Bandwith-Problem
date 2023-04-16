import parser, dichotomie
import sys
from os import listdir, cpu_count
import subprocess
import signal


def main(argv):

    # cpuc = cpu_count()
    # if cpuc != None:
    #     nproc = int((1/2) * cpuc)
    # else:
    #     nproc = 1

    # print("Model used is : ", sys.argv[1])

    # Parse all HB113 files into json files
    # parser.read_all_data()

    # Define the path to the folder containing the files to be processed
    folder_path = "../data/"

    # Get a list of all the files in the specified folder
    # file_list = os.listdir(folder_path)

    # Filter out any files that don't end in ".json"
    # file_list = [file for file in file_list if file.endswith(".json")]
    # print(len(file_list))

    # Test sur une instance non concluante
    dichotomie.run_dicho_solver("bcspwr01.json", "model2", 60)


if __name__ == '__main__':
    main(sys.argv[0:])

