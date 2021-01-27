import cProfile
import glob

files = glob.glob('F:/cProfile/*.py', recursive = False) 
for file in files: 
    print(file)
    run_cProfile(file)