from subprocess import call
from glob import glob
from sys import argv, setrecursionlimit
from os import path

setrecursionlimit(10000)
files = glob('**/*.py', recursive=False)

def run_cProfile(file):
    call(['python', '-m', 'cProfile', '-s', 'ncalls', file])

for file in files:
    _, startname = path.split(argv[0])
    if file == startname:
        continue
    print('Processing file: {}'.format(file))
    run_cProfile(file)