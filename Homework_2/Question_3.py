# Brian Powell 012362894
# EE381 - Chaw-Long Chu
#
# Homework_2
# 
# Question_3
# For a (5x5) transition matrix given as following, please find the limiting matrix:
# [ 1  0  0  0  0]
# [ 0  1  0  0  0]
# [ 0  0  1  0  0]
# [.1 .2 .3  0 .4]
# [.2 .4  0 .2 .2]

import numpy as np 

P = np.matrix([[ 1,  0,  0,  0,  0],
               [ 0,  1,  0,  0,  0],
               [ 0,  0,  1,  0,  0],
               [.1, .2, .3,  0, .4],
               [.2, .4,  0, .2, .2]])

print("Matrix P")
print(P)

n = 12
Pn = P**n

np.set_printoptions(precision=4, suppress=True)
print("\nTransition Matrix of P")
print(Pn)


################## End of Question 3 ################## 