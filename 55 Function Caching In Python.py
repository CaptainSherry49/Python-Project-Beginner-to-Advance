import time
from functools import lru_cache


# @lru_cache(maxsize=3)
# def some_work(n):
#     print(f'Sir You enter {n}, which kind of number is this. ')
#     time.sleep(n)
#     return n
#
#
# if __name__ == '__main__':
#     print('Executing Some Work')
#     some_work(5)
#     print('Done.... Calling Again')
#     some_work(5)
#     some_work(5)
#     some_work(5)
#     some_work(5)
#     print('called again')



# ---------- Task ---------- #
user = int(input('How many values you want to cache ? '))


@lru_cache(maxsize=user)
def task():
    print('Task....')


print(0)
task()
print(1)
task()
print(2)
task()
print(3)
task()
