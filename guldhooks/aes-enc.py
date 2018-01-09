#! /usr/bin/env python2
from subprocess import check_output
from os import listdir, getcwd
from common import getFiles, get_pass, generate_pass


def getFilesToEncrypt():
    return check_output(["git", "ls-files", "--others", "--exclude-standard"])  #  | grep -o '\S*$'


def encryptFile(f, p):
    return check_output(["openssl", "aes-256-cbc", "-a", "-in", f, "-out", "%s.aes.enc" % f, "-pass", "pass:%s" % p])


def decryptFile(f, p):
    return check_output(["openssl", "aes-256-cbc", "-d", "-a", "-in", " %s.aes.enc" % f, "-out", f, "-pass", "pass:%s" % p])

def encryptAll(f):
    
    return

if __name__ == "__main__":
    print(getFilesToEncrypt())
    
    #p = generate_pass("/people/isysd/.keepass-aes")
    p = get_pass("/people/isysd/.keepass-aes")
    print(encryptFile('deginner.kdb', p))
