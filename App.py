from pathlib import Path


def main():
    val = 1
    directories = []
    path = Path()
    savePath = []
    while val == 1:
        for file in path.iterdir():
            if file.is_dir():
                print("Save path to " + file.name)
                directories.append(file.name)
            else:
                print("File: " + file.name)
        if len(directories) > 0:
            file = directories[0]
            path = Path(file)
            savePath.append(file)
            print("Change path to " + file)
            directories.remove(file)
        else:
            print(savePath)
            savePath.pop()
            if len(savePath) == 0:
                val = 0


if __name__ == "__main__":
    main()
