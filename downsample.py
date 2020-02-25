#Downsample at desired percent.
import time
start_time = time.time()

import sys
input_path  = sys.argv[1]
output_path = sys.argv[2]
percent = int(sys.argv[3])

import random

newfile = open(output_path,'w')

with open(input_path, 'r') as output:
    while True:
        record = list(output.readline()[:-1] for index in range(8))
        if len(record[0]) == 0:
            break
        if random.randrange(1,101) <= percent:
            newfile.write("\n".join(record))
            newfile.write("\n")

newfile.close()

print("splited ---%s seconds ---" % (time.time() - start_time))