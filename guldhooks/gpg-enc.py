#! /usr/bin/env python2
from subprocess import check_output
from os import listdir, getcwd
from common import getFiles, get_pass, generate_pass, getFingerprint, getGuldHooks, mkdirp
import argparse

def hasgpg(hook):
    if 'gpg' not in hook:
        return True
    return False

def getFilesToEncrypt():
    allf = getGuldHooks()
    if not allf:
        return []
    return filter(hasgpg, allf)

def encryptFile(f, recipients=None):
    me = getFingerprint()
    if recipients is None:
        recipients = [me]
    cmd = ["gpg", "-ae", "--batch", "--yes", "-u", me, "-o", "./.blocktree/%s.gpg" % f]
    for r in recipients:
        cmd = cmd + ['-r', r]
    cmd = cmd + [f]
    return check_output(cmd)


def decryptFile(f, recipients=None):
    me = getFingerprint()
    if recipients is None:
        recipients = [me]
    cmd = ["gpg", "-a", "--batch", "--yes", "-u", me, "-o", f]
    for r in recipients:
        cmd = cmd + ['-r', r]
    cmd = cmd + ["./.blocktree/%s.gpg" % f]
    return check_output(cmd)

def encryptAll():
    for f in getFilesToEncrypt():
        encryptFile(f)

def decryptAll():
    for f in getFilesToEncrypt():
        decryptFile(f)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["encrypt", "decrypt"], help="Command to run.")
    #parser.add_argument("--verbosity", help="increase output verbosity")
    args = parser.parse_args()

    if args.command == 'encrypt':
        mkdirp('./.blocktree')
        encryptAll()
    elif args.command == 'decrypt':
        decryptAll()
    else:
        exit(1)

    #p = generate_pass("/people/isysd/.keepass-aes")
    #p = get_pass("/people/isysd/.keepass-aes")
    #print(encryptFile('deginner.kdb'))
