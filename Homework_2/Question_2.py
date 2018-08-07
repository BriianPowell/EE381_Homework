# Brian Powell 012362894
# EE381 - Chaw-Long Chu
#
# Homework_2
#
# Question_2
# For a (6x6) transition matrix given as following, please find the limiting matrix:
# [ 1  0  0  0  0  0]
# [ 0  1  0  0  0  0]
# [ 0  0  1  0  0  0]
# [.1 .2 .3  0 .1 .3]
# [.2 .4  0 .2 .2  0]
# [.1  0  0 .3 .3 .3]

import numpy as np

P = np.matrix([[ 1,  0,  0,  0,  0,  0],
               [ 0,  1,  0,  0,  0,  0],
               [ 0,  0,  1,  0,  0,  0],
               [.1, .2, .3,  0, .1, .3],
               [.2, .4,  0, .2, .2,  0],
               [.1,  0,  0, .3, .3, .3]])

print("Matrix P")
print(P)

n = 25
Pn = P**n

np.set_printoptions(precision=4, suppress=True)
print("\nLimiting Matrix of P")
print(Pn)


################## End of Question 2 ################## 