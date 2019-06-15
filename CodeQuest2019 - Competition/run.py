import os
import traceback

n = "0"
while True:
    try:
        n = (input() or n).zfill(2)
        os.system(f"python Prob{n}.py < Prob{n}.in.txt")
    except:
        traceback.print_exc()
