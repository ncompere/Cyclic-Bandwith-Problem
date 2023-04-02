import parser
import sys
import os
import subprocess
import signal

def main(argv):
    print("Model used is : ", sys.argv[1])
    # parser.read_data_v2(file=sys.argv[1])

    # PARSE ALL HB113 INSTANCES
    # for file_name in os.listdir("../HB113/"):
    #     if file_name.endswith(".rnd"):
    #         print(os.path.join("../HB113/", file_name))
    #         parser.read_data_v2(file=os.path.join("../HB113/", file_name))

    # Define the path to the folder containing the files to be processed
    folder_path = "../data/"

    # Get a list of all the files in the specified folder
    file_list = os.listdir(folder_path)

    # Filter out any files that don't end in ".json"
    file_list = [file for file in file_list if file.endswith(".json")]
    print(len(file_list))

    # Loop over the file list and execute the Python script for each file
    for file in file_list:
        # Construct the command to run the Python script with the file as an argument
        if sys.argv[1] == "model1":
            command = ["python3", "model1.py", "-data=" + os.path.join(folder_path, file), "-solve"]
        if sys.argv[1] == "model2":
            command = ["python3", "model2.py", sys.argv[2], "-data=" + os.path.join(folder_path, file), "-solve"]
        # Launch the Python script as a subprocess with the specified arguments
        subprocess.call(command)


if __name__ == '__main__':
    main(sys.argv[0:])

