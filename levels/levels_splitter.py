i = 0
buffer = ''
with open("raw_levels.txt") as file:
    for k in file.readlines():
        if k == "*************************************\n":
            with open(f"{i}.txt", 'w') as out:
                out.write(buffer)
                buffer = ''
                i += 1
        else:
            if not k.startswith(("Maze", "File", "End", "Length")) and k != '\n':
                buffer += k
