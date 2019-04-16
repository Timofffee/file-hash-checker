import hashlib
import time
from pathlib import Path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path', help='path to folder', default='./')
parser.add_argument('-i', '--input', help='input file (default: ./hashes)', default='./hashes')
parser.add_argument('-o', '--output', help='output file (default: ./corrupted_files.txt)', default='./corrupted_files.txt')
parser.add_argument('-b', '--bytes', help='Bytes size for read files (default: 8192)', default=8192, type=int)
args = parser.parse_args()

if args.path[-1] != '/':
    args.path += '/'

corrupted_file = []
output = open(args.output, 'w')

start_time = time.time()
hashes = open(args.input, 'r')
    

while True:
    l = hashes.readline()
    if l == '':
        break
    
    file_name, original_md5 = l.split(" ")
    original_md5 = original_md5.split()[0]

    c_file = Path(file_name)
    if not c_file.is_file():
        print("File {file} is not found!".format(file=file_name))
        continue
    with open(file_name, 'rb') as file_to_check:
        returned_md5 = hashlib.md5()
        for chunk in iter(lambda: file_to_check.read(args.bytes), b""):
            returned_md5.update(chunk)

        returned_md5 = returned_md5.hexdigest()
        print("Checking {file}\nCorrect md5: {orig_md5}\nFile md5: {ret_md5}".format(file=file_name, orig_md5=original_md5, ret_md5=returned_md5))
        if original_md5 == returned_md5:
            print('MD5 verified.\n')
        elif original_md5 != returned_md5:
            print("MD5 verification failed!.\n")
            corrupted_file.append(file_name)


print("Errors: {count}".format(len(corrupted_file)))
print("--- {time} seconds ---".format(time.time() - start_time))

output.write('Corrupted files: \nTo be sure, check with another program! \n')
for c in corrupted_file:
    output.write(c + '\n')
    print(c)
