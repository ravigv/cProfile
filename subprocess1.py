import cProfile
import glob
import subprocess

files = glob.glob('F:/cProfile/*.py', recursive = False) 
for file in files: 
    print(file)
    subprocess.call(['python', '-m', 'cProfile', '-s', 'ncalls', file])