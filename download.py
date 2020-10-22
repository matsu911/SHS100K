import os
import subprocess

def main():
    data = [x.split("\t") for x in open('./list').readlines()]
    for item in data:
        subprocess.call(["youtube-dl", item[4],
                         '-o', os.path.join('SHS100K-dataset', item[0], "%s.mp3" % item[1]),
                         '-x',
                         '--audio-format', 'mp3'])

if __name__ == '__main__':
    main()
