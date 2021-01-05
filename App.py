from pathlib import Path
import sys, getopt
from shutil import copyfile


def main(argv):
    val = 1
    if len(argv) >= 3:
        startDir = str(argv[0])  # "C:\\WorkFolder\\ADC_IoT\\GenXStaticLibrary"
        copyDir = str(argv[1])  # "C:\\WorkFolder\\ADC_IoT\\ADCN_Proj"
        LookUpExtention = argv[2:]
    else:
        print("Wrong number of parameters")
        exit
    copyFileCounter = 0
    PathCounter = 0
    directories = []
    path = Path(startDir).resolve()
    print("The source path: " + str(path))
    copyPath = ""
    if not Path(copyDir).exists():
        Path(copyDir).mkdir()
    while val == 1:
        # iterate on all files to find
        for file in path.iterdir():
            copyPath = str(file.resolve()).replace(startDir, copyDir)
            if file.is_dir():
                if copyPath.find(".") == -1:
                    # save directory full path
                    directories.append(str(file.resolve()))
                    if not Path(copyPath).exists():
                        # Create directory in copy folder
                        Path(copyPath).mkdir()
                        # print("Create path: " + copyPath)
            else:
                doCopy = False
                for ext in LookUpExtention:
                    if copyPath.find(str(ext)) != -1:
                        doCopy = True
                        break
                if doCopy == True:
                    copyFileCounter += 1
                    copyfile(str(file.resolve()), copyPath)
                # print("Copy File from " + str(file.resolve()) + " to " + copyPath)
        if len(directories) > 0:
            file = directories[0]
            path = Path(file)
            # print("New path to: " + file)
            directories.remove(file)
            PathCounter += 1
        else:
            print(
                "In "
                + str(PathCounter)
                + " directories "
                + str(copyFileCounter)
                + " files was copied"
            )
            val = 0


if __name__ == "__main__":
    main(sys.argv[1:])
