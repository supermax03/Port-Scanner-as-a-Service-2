import time
import random
import string
import hashlib


def makesalt():
    salt = ""
    for i in range(10):
        salt = salt + random.choice(string.ascii_letters)
    return salt


def gethash():
    h = hashlib.md5()
    h.update((time.clock().__str__() + makesalt()).encode('utf-8'))
    return h.hexdigest()
