import os

def fun(path, extension):
    try:
        os.chdir(path)
    except:
        print("No such file exit")
        exit()

    files = os.listdir(path)
    print(files)
    s = [os.path.splitext(h)[1] for h in files]
    print(s)
    if extension not in s:
        print(f"{extension} not in {path} directory")
        exit()

    i=0
    for filename in files:
        split = os.path.splitext(filename)[1]
        # print(split)

        if split == extension:
            try:
                os.rename(filename, f"{i}{extension}")
            except:
                os.rename(filename, f"{i+1}{extension}")

            print(os.listdir(path))
            i += 1


path = input("enter path: ")
extension = input("enter: ")

fun(path=path, extension=extension)
