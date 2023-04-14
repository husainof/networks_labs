#!/usr/bin/python3

import argparse
import ftplib
import pprint

g_tree = ''

def traverse(ftp):
    
    level = {}
    for entry in (path for path in ftp.nlst()):
        try:
            ftp.cwd(entry)
            level[entry] = traverse(ftp)
            ftp.cwd('..')
        except ftplib.error_perm:
            level[entry] = None
    return level


def generate_tree(tree, n=0):
    global g_tree
    for el in tree:
        if tree[el] is None:
            g_tree +=  '    |' * n + '-' * 4 + el + '\n'
        elif len(tree[el]):
            g_tree += '    |' * n + '-' * 4 + el + '\\' + '\n'
            generate_tree(tree[el], n+1)


def get_tree(host, login, password):
    # parser = argparse.ArgumentParser(description='Print tree ftp directory')
    # parser.add_argument("-ip", default='91.222.128.11', help="set ip address", type=str)
    # parser.add_argument("-l", default='testftp_guest', help="set login", type=str)
    # parser.add_argument("-p", default='12345', help="set password", type=str)
    # parser.add_argument("-d", default=0, help="set depth", type=int)

    # args = parser.parse_args()
    ftp = ftplib.FTP(host)
    ftp.login(login, password)
    tree = traverse(ftp)
    generate_tree(tree)
    global g_tree
    return g_tree
    # pprint.pprint(tree)
