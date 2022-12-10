with open("input-07.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# # Example input:
# lines = """$ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k
# """.splitlines()


# Example answer = 95437


class Dir:
    def __init__(self, name=""):
        self.name = name
        self.sub_dirs = {}
        self.files = {}

    def size(self):
        return sum(self.files.values()) + sum([d.size() for d in self.sub_dirs.values()])


def get_cwd():
    return current_path[len(current_path) - 1]


root = Dir()
current_path = [root]
all_dirs = {root}

for line in lines:
    if line.startswith('$'):
        cmd = line[2:]
        if cmd.startswith("cd"):
            dir_name = cmd[3:]
            if dir_name == "/":
                current_path = [root]
            elif dir_name == "..":
                if len(current_path) > 1:
                    current_path.pop()
            else:
                if dir_name not in get_cwd().sub_dirs:
                    get_cwd().sub_dirs[dir_name] = Dir(dir_name)
                dir = get_cwd().sub_dirs[dir_name]
                current_path.append(dir)
                all_dirs.add(dir)
        elif cmd.startswith("ls"):
            pass
    else:
        if line.startswith("dir"):
            dir_name = line[4:]
            if dir_name not in get_cwd().sub_dirs:
                get_cwd().sub_dirs[dir_name] = Dir(dir_name)
        else:
            size, filename = line.split()
            get_cwd().files[filename] = int(size)

space_needed = root.size() - (70000000 - 30000000)
big_enough_dirs = set()
for dir in all_dirs:
    if dir.size() >= space_needed:
        big_enough_dirs.add(dir)
print(min([dir.size() for dir in big_enough_dirs]))
