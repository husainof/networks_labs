#!/usr/bin/python3

import argparse
import ftplib
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
    parser = argparse.ArgumentParser(description='Print tree ftp directory')
    parser.add_argument("-ip", default='91.222.128.11', help="set ip address", type=str)
    parser.add_argument("-l", default='testftp_guest', help="set login", type=str)
    parser.add_argument("-p", default='12345', help="set password", type=str)
    parser.add_argument("-d", default=0, help="set depth", type=int)

    args = parser.parse_args()
    ftp = ftplib.FTP(args.ip)
    ftp.login(args.l, args.p)
    tree = traverse(ftp)
    generate_tree(tree, args.d)
    # pprint.pprint(tree)


if __name__ == '__main__':
    main()
