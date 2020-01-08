"""
Question 3
Complexity : n
"""
import time

string = "BennettUniversity"
string = list(string)

n = input("Enter N : ")
while(n.isnumeric() == False):
    print("Enter a Number !")
    n = input("Enter N : ")

n = int(n)

if(n <= 0 or n > len(string)):
    print("Enter a Valid Number !")

start_time = time.time()
for chInd in range(len(string)):
    if (chInd+1) % n == 0:
        string[chInd] = string[chInd].upper()

print(''.join(string))
print("--- %s seconds ---" % (time.time() - start_time))
