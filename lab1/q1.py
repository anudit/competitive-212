"""
Question 1
Complexity : n^2
"""
import time

left = 10
right = 20
digits = [1, 2, 3, 7]
correct = 0

skips = []
num = 0

start_time = time.time()
for num in [x for x in range(left, right) if x not in skips] :
    if(num in skips):
        continue
    for digit in digits:
        loc = str(num)[::-1].find(str(digit))
        if (loc%2 == 0):
            correct += 1
            if (loc == len(str(num))-1):

                new_num = list(str(num))
                new_num[0] = str(int(new_num[0])+1)
                new_num = int(''.join(new_num))

                # print(f"NUM : {num} NEW_NUM : {new_num} len : {len(skips)}")
                skips = skips + list(range(num, new_num))
                correct += (new_num - num)
                if(new_num > right):
                    correct += (right - new_num - 1)
            break

print(correct)
print("--- %s seconds ---" % (time.time() - start_time))

# 100%|██████████| 999999/999999 [07:34<00:00, 2199.71it/s]742204
