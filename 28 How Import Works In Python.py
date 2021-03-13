# ------------------------- Import Works ? ------------------- #
# import pandas as pd
# print(pd.__version__)
#
# import sys
# print(sys.path)  # Kaha sa sara module import hota ha


# ----------------------------- importing internal Files ------------- #
import File1
print(f'A is {File1.a}')
print()
print(f'B is {File1.b}')

print(File1.name.__doc__)
File1.name('Sherry')

