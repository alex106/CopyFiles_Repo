from pathlib import Path
import sys, getopt
from shutil import copyfile

RemoveCounter = 0


def main(argv):
    val = 1
    sourceDir = ""
    destDir = ""
    LookUpExtention = []
    if len(argv) >= 3:
        sourceDir = str(argv[0]).strip()  # "\\ADC_IoT\\GenXStaticLibrary"
        destDir = str(argv[1]).strip()  # "\\ADC_IoT\\ADCN_Proj"
        LookUpExtention = argv[2:]
    else:
        print("Wrong number of parameters")
        exit
    copyFileCounter = 0
    PathCounter = 0
    directories = []
    path = Path(sourceDir).resolve()
    print("The source path: " + str(path))
    copyPath = ""
    if not Path(destDir).exists():
        Path(destDir).mkdir()
    print("The destanation path: " + destDir)
    while val == 1:
        # iterate on all files to find
        for file in path.iterdir():
            copyPath = str(file.resolve()).replace(sourceDir, destDir)
            if file.is_dir():
                if copyPath.find(".") == -1:
                    # save directory full path
                    directories.append(str(file.resolve()))
                    if not Path(copyPath).exists():
                        # Create directory in copy folder
                        Path(copyPath).mkdir()
                        # print("Create path: " + copyPath)
            else:
                if is_extention(copyPath, LookUpExtention, False):
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
            remove_empty_dir(destDir, LookUpExtention)
            val = 0


def remove_empty_dir(directory, LookUpExtention):
    isNotEmpty = False
    if not Path(directory).exists():
        exit
    path = Path(directory).resolve()
    for file in path.iterdir():
        if not file.is_dir():
            isNotEmpty = True
        else:
            if is_extention(str(file.resolve()), LookUpExtention, True):
                isNotEmpty = True
            else:
                if not remove_empty_dir(str(file.resolve()), LookUpExtention):
                    Path(file).rmdir()
                else:
                    isNotEmpty = True
    return isNotEmpty


def is_extention(fileName, Extentions, isDir):
    for ext in Extentions:
        isDot = False
        if str(ext).find(".") != -1:
            isDot = True
        if isDir != isDot:
            if fileName.find(str(ext).strip()) != -1:
                return True
    return False


if __name__ == "__main__":
    main(sys.argv[1:])
