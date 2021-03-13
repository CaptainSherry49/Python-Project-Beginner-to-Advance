# # ---------------------------------- Time Module --------------------------- #

import time

t1 = time.time()

k = 0
while k < 55:
    print('*_*')
    k += 1
print(f'While loop ran in {time.time() - t1}')
print('__________________________')


t2 = time.time()

for i in range(55):
    print('#(*)_(*)#')

print(f'For loop ran in {time.time() - t2}')


local = time.asctime(time.localtime(time.time()))
print(local)


# -------------------------- time.sleep() ----------------- #
for i in range(10):
    time.sleep(3)  # time.sleep make a delay of how many seconds you want
    print('#ban_haqeeqat_tv')