import ftplib
import json
import pprint


def traverse(ftp, depth=0):
    if depth > 10:
        return ['depth > 10']
    level = {}
    for entry in (path for path in ftp.nlst() if path not in ('.', '..')):
        try:
            ftp.cwd(entry)
            level[entry] = traverse(ftp, depth+1)
            ftp.cwd('..')
        except ftplib.error_perm:
            level[entry] = None
    return level


def generate_tree(tree, n=0):
    for el in tree:
        if tree[el] is None:
            print('    |' * n + '-' * 4 + el + '\n'.rstrip('\n'))

        elif len(tree[el]):
            print('    |' * n + '-' * 4 + el + '\\' + '\n'.rstrip('\n'))
            generate_tree(tree[el], n+1)


def main():
    ftp = ftplib.FTP('91.222.128.11')
    ftp.login('testftp_guest', '12345')
    tree = traverse(ftp, 4)
    generate_tree(tree)
    # pprint.pprint(tree)


if __name__ == '__main__':
    main()
