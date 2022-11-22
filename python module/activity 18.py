#!/usr/bin/env python3

def linenums(inpath, outpath):
    # with pen inpath as fi,
    fi = open(inpath, 'r')
    fo = open(outpath, 'w')
    for i, line in enumerate(fi.readlines()):
        tmp = line
        tmp = f'{i+1}: ' + tmp
        fo.write(tmp)
    fi.close()
    fo.close()


# fp = open('/home/usacys/python/python-1/rosso/outpath', 'r')
# print(fp.read())
linenums('/home/usacys/python/python-1/rosso/inpath', '/home/usacys/python/python-1/rosso/outpath')