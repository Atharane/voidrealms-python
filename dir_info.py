# Simple application that scans a directory recursively & displays the basic info

import os

stats = dict(path='', folders=0, files=0, links=0, size=0)


# Get user input
def get_input():
    global stats
    i_path = os.path.abspath(input('Directory path: '))

    if not os.path.exists(i_path):
        print('Path does not exist!')
        exit(1)

    if not os.path.isdir(i_path):
        print('Path is not a directory!')
        exit(2)

    stats['path'] = i_path


# Scan the path recursively
def scan(path):
    global stats
    print(f'Scanning {path}...\n')

    for root, dirs, files in os.walk(path, onerror=None, followlinks=False):
        stats['folders'] += len(dirs)
        stats['files'] += len(files)
        for name in files:
            fullname = os.path.join(root, name)
            size = os.path.getsize(fullname)
            stats['size'] += size


def display():
    global stats
    print('Results:')
    for k, v in stats.items():
        print(f'{k}: {v}')


def main():
    global stats
    get_input()
    scan(stats['path'])
    display()


if __name__ == "__main__":
    main()
