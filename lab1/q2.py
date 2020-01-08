"""
Question 2
Complexity : n
Test input :  20 21 22 23 24 25 26 27 28 29 30
"""
import time

current_seq = list(map(int, input("Enter Sequence: ").split()))
print(current_seq)
current_seq = current_seq[::-1]

counters = input("Enter the number of counters : ")
while(counters.isnumeric() == False):
    print("Enter a Number !")
    counters = input("Enter the number of counters : ")

counters = int(counters)
if(counters > len(current_seq)):
    print("Enter a Smaller Number!")
    exit()

new_seq = []

for i in range(counters):
    new_seq.append([])

cnt=0
i=0

start_time = time.time()
while (cnt < len(current_seq)):
    new_seq[i] = new_seq[i] + [current_seq[cnt]]

    if (counters - 1 == i):
        i = 0
    else:
        i+= 1

    cnt+= 1

print(new_seq)
print("--- %s seconds ---" % (time.time() - start_time))
