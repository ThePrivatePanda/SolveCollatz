import time
def get_nums():
    with open("nums.txt") as file:
        return file.readlines()

def write_num(num):
    with open("nums.txt", "a") as file:
        file.write(num)

ab = time.time()
for i in range(1, 101):
    get_nums()
print(time.time()-ab)

cd = time.time()
for i in range(1, 101):
    write_num(f"\n{i}")
print(time.time()-cd)

print(get_nums())
ef = time.time()
for i in range(1, 101):
    skem = f"{i}\n"
    print(f"{skem in get_nums()}")
print(time.time()-ef)


idk = time.time()
for i in range(1, 25000):
    before = time.time()

    x = i
    stl = []
    print(x)

    while x != 4 and x not in get_nums():
        if x % 2 == 0:
            x = x/2
        else:
            x = (3*x)+1
        stl.append(x)
    print(time.time()-before)

print(time.time()-idk)