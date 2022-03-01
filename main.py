import threading
import time
solved = []

def workit(start, end):
    for i in range(start, end):
        x = i
        nums = []

        while x != 1 and x not in solved:
            if x % 2 == 0:
                x = x/2
            else:
                x = (3*x)+1
            nums.append(x)

        solved.append(nums)

workit(1, 1000)
