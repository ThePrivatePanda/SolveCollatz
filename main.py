import time

stl = []
try:
    starting = time.time()
    for i in range(1, 111111):
        x = i

        while x not in stl:
            if x % 2 == 0:
                x = x/2
            else:
                x = (3*x)+1
            if x not in stl:
                stl.append(x)
except KeyboardInterrupt:
    print(stl)
    print(i)
    print(time.time()-starting)
    raise SystemExit
