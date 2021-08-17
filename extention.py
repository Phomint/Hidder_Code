def recover_file():
    with open('main.py', 'r', encoding='utf-8') as f:
        file = []
        for line in f.readlines():
            if 'extention' not in line:
                file.append(line)

    with open('main.py', 'w', encoding='utf-8') as f:
        f.write(''.join(file))

def hidding():
    pass