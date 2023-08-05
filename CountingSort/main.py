import datetime
from numpy.random import seed
from numpy.random import randint
import numpy as np

def countSort(arr):
    output = [0 for i in range(len(arr))]
    count = [0 for i in range(51)]
  
    for i in arr:
        count[i] += 1
 
    for i in range(1, 51):
        count[i] += count[i-1]
  
    for i in range(len(arr)):
        output[count[arr[i]]-1] = arr[i]
        count[arr[i]] -= 1
    return output


# seed random number generator
seed(1)
# generate some integers
x = [100,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000]
t = []
for i in x:
    arr = randint(1, 10, i)
    start_time = datetime.datetime.now()
    ans = countSort(arr)
    end_time = datetime.datetime.now()
    time_diff = (end_time - start_time)
    execution_time = time_diff.total_seconds() * 100
    t.append(execution_time);

print(t)
# print(ans)