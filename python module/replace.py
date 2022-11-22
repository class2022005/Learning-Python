#!/usr/bin/env python3

with open('/etc/passwd') as fi, open('passwd.txt', 'w') as fo: #file in (reads the /file/path, file out gives the output of /file/path on the new file
    for line in fi:
        # line.replace('/bin/bash\n', '/bin/fsh/\n')
        tmp = line.split(':')
        tmp[-1] = '/bin/fish\n'
        fo.write(':'.join(tmp))
    else:
        fo.write(line)