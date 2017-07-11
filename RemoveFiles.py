#coding=gbk

import os

imgPostfix = ".png", ".jpg", ".jpeg", ".gif", ".bmp", ".psd", ".ico", ".svg"

print "start..."

def removeEmptyDir(d):
    ls = os.listdir(d)
    if len(ls) == 0:
        os.rmdir(d)
        return
    for f in ls:
        p = d + "/" + f
        if os.path.isdir(p):
            removeEmptyDir(p)

def removeNotImg(d):
    ls = os.listdir(d)
    for f in ls:
        p = d + "/" + f
        if os.path.isdir(p):
            removeNotImg(p)
        else:
            if not isImage(f):
                print f
                os.remove(p)

def isImage(f):
    for p in imgPostfix:
        if f.lower().endswith(p):
            return True
    return False

dir = "D:\\WebRoot"
removeNotImg(dir)
removeEmptyDir(dir)

print "finish"
