import time
import random
import string
import hashlib
import datetime


def makesalt():
    salt = ""
    for i in range(10):
        salt = salt + random.choice(string.ascii_letters)
    return salt


def gethash():
    h = hashlib.md5()
    h.update((time.clock().__str__() + makesalt()).encode('utf-8'))
    return h.hexdigest()

def isexpiredtoken(updated_on):
    time = (datetime.datetime.now() - updated_on).total_seconds()
    result=False
    if (time>3600):
             result=True
    return result