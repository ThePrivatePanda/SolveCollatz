from os import pipe
import time

stl = []
try:
    idk = time.time()
    for i in range(1, 111111):
        x = i

        while x != 4 and x not in stl:
            if x % 2 == 0:
                x = x/2
            else:
                x = (3*x)+1
            if x not in stl:
                stl.append(x)
except KeyboardInterrupt as e:
    print(stl)
    print(i)
    print(time.time()-idk)
    quit()
