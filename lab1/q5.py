"""
Question 5
Complexity : n
"""
import sys
import time

l = [2, 5, 10, 13, 23, 30, 32, 40, 60, 70]

x = input("Enter x : ")
while(x.isnumeric() == False):
    print("Enter a Number !")
    x = input("Enter x : ")

x = int(x)

mini = 0
minv = sys.maxsize

ind = 0

start_time = time.time()

if (x >= l[-1]):
    print(l[-1])
    print("--- %s seconds ---" % (time.time() - start_time))
    exit()

while ind < len(l):
  if (abs(l[ind] - x) < minv):
    mini =  ind
    minv = abs(l[ind] - x)
  ind+=1

print(l[mini])
print("--- %s seconds ---" % (time.time() - start_time))

