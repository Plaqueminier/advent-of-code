def cd(pwd, path):
    if path == "/":
        return "/"
    if path == "..":
        return pwd[: pwd.rfind("/")]
    return pwd + "/" + path if pwd != "/" else pwd + path


def calc_dir_size(files, path):
    size = 0
    for file in files[path]:
        if file[0] == "dir":
            size += calc_dir_size(
                files, path + "/" + file[1] if path != "/" else path + file[1]
            )
        else:
            size += int(file[0])
    return size


def one():

    with open("input.txt") as f:
        lines = [line for line in f]

    pwd = "/"
    files = {"/": []}
    for line in lines:
        line = line.strip()
        if line[0] == "$":
            command = line.split(" ")
            if command[1] == "cd":
                pwd = cd(pwd, command[2])
            else:
                continue
        else:
            file = line.split(" ")
            if not pwd in files.keys():
                files[pwd] = []
            files[pwd].append((file[0], file[1]))
    print(files)

    sum_one = 0
    files_two = []
    for dir in files:
        if calc_dir_size(files, dir) < 100000:
            sum_one += calc_dir_size(files, dir)
        if calc_dir_size(files, dir) >= calc_dir_size(files, "/") - 40000000:
            files_two.append((dir, calc_dir_size(files, dir)))
    print(sum_one)
    print(min(files_two, key=lambda x: x[1]))


if __name__ == "__main__":
    one()
