import os, hashlib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path', help='path to folder', default='./')
parser.add_argument('-o', '--output', help='output file (default: "./hashes")', default='./hashes')
parser.add_argument('-b', '--bytes', help='Bytes size for read files (default: 8192)', default=8192, type=int)
args = parser.parse_args()

if args.path[-1] != '/':
    args.path += '/'

hashes = []
output = open(args.output, 'w')


for top, dirs, files in os.walk(args.path):
    for nm in files:
        file_name = os.path.join(top, nm).replace("\\", "/")
        with open(file_name, 'rb') as file_to_check:
            md5_r = hashlib.md5()

            for chunk in iter(lambda: file_to_check.read(args.bytes), b""):
                md5_r.update(chunk)
            md5_returned = md5_r.hexdigest()
            hashes.append([file_name[len(args.path):], md5_returned])

print("Files: " + str(len(hashes)))

for h in hashes:
    output.write(' '.join(h) + '\n')
    print(' '.join(h))