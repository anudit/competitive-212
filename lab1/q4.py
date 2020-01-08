"""
Question 4
Complexity : n
"""
import time

ini_pos = input('Enter Original Location: ')
while(ini_pos.isnumeric() == False):
    print("Enter a Number !")
    ini_pos = input('Enter Original Location: ')
ini_pos = int(ini_pos)
if (ini_pos > 1000):
    print("Enter a Smaller Number !")
    exit()


step = input('Enter Step Size: ')
while(step.isnumeric() == False):
    print("Enter a Number !")
    step = input('Enter Step Size: ')
step = int(step)

steps = [ini_pos]

def jump(cur_pos, step_value, side, steps):
    if cur_pos > ini_pos:
        return steps
    elif side == -1: # Negative Side
        cur_pos += step_value
        if not cur_pos > ini_pos:
            steps.append(cur_pos)
    elif side == 1: # Positive Side
        cur_pos -= step_value
        if cur_pos <= 0:
            side = -1
        steps.append(cur_pos)
    return jump(cur_pos, step_value, side, steps)

start_time = time.time()
print(jump(ini_pos, step, 1, steps))
print("--- %s seconds ---" % (time.time() - start_time))
