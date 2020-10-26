import os
import subprocess
import itertools

def flatten(l):
    return list(itertools.chain.from_iterable(l))

def comp(x, y):
    a = cmp(x[0], y[0])
    if a != 0:
        return a
    return cmp(x[1], y[1])

def detect_latest():
    tmp = [[os.path.join(root, f) for f in files]
           for root, dirs, files in os.walk(top='SHS100K-dataset')]
    tmp = flatten(tmp)
    if len(tmp) == 0:
        return (0, 0)
    tmp = [x.split("/")[1:] for x in tmp]
    tmp = [(int(a), int(b[:-4])) for a,b in tmp]
    latest = sorted(tmp)[-1]
    return latest

def main():
    set_id, ver_id = detect_latest()

    data = [x.split("\t") for x in open('./list').readlines()]
    for item in data:
        if int(item[0]) < set_id:
            continue
        if int(item[0]) == set_id and int(item[1]) <= ver_id:
            continue
        if not bool(item[5]): continue
        subprocess.call(["youtube-dl", item[4],
                         '-o', os.path.join('SHS100K-dataset', item[0], "%s.mp3" % item[1]),
                         '--sleep-interval', '120',
                         '-x',
                         '--audio-format', 'mp3'])

if __name__ == '__main__':
    main()
