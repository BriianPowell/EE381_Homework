# Brian Powell 012362894
# EE381 - Chaw-Long Chu
#
# Homework_2 (Markov Chain)
# 
# Question 1
# 4 supermarkets(A,B,C,D) working on advertisement to get higher market share. 
# After several months, it is found a stable transition was established as follows:
# 30% of A stay with A, 10% changes to B, 30% changes to C, rest change to D
# 20% of B change to A, 35% stays with B, none change to C, rest change to D
# Both C and D keep all customers

import numpy as np
np.set_printoptions(precision=4,suppress=True)

# Part 1
# Prepare a Transition Matrix
P = np.matrix([[.3,.1,.3,.3],
               [.2,.35,0,.45],
               [0,0,1,0],
               [0,0,0,1]])

print("Matrix P")
print(P)

# Part 2
# Get the imit transition matrix
n = 15
Pn = P**n
print("\nLimit Transition Matrix of P")
print(Pn)

# Part 3
# If market share begins with A=0.3, B=0.3, C=0.15,D=0.25, please find the stable marke share.
D = np.matrix([.3,.3,.15,.25])
print("\nStabilizing Matrix of P")
print(np.dot(D, Pn))

################## End of Question 1 ################## 