# File Hash Chacker
Simple scripts to check file integrity with md5.

## How to use
You can generate a file that will contain a list of files and their hashes. To do this, run the file `gen.py` ( `python gen.py` ).

This will generate a file `hashes` with the desired content. 
For example:
```
check.py 66c5814113dc104321471bcb3fe6081a
gen.py 4ca0f4386a513fb3523181f7328c2d0b
LICENSE 6db65a4009fa4f583c7279cafec26a59
README.md 59380d65b5145531e44f5ef6953e7c40
```

After that you can run `check.py` ( `python check.py` ) for verification.

## More
Use arguments to make scripts work better.
### Custom path to folder and output hashes in file.txt
```python gen.py -p ./path/to/ -o file.txt```
### Custom path to folder, file with hashes and output in out.txt
```python check.py -p ./path/to/ -i file.txt -o out.txt```