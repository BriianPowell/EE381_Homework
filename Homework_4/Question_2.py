# Brian Powell 012362894
# EE381 - Chaw-Long Chu
#
# Homework_4
#
# Question_2
# Using random number to generate 2000 numbers from (-1 to 1) and find mean, standard deviation, variance of these 200 numbers, and plot histogram of these 2000 numbers
#

import random as rand
import matplotlib.pyplot as plt
import numpy as np


x = [rand.uniform(-1,1) for x in range (2000)]

print("Homework 4")
print("Question 2")

print("\nMean of generate random numbers:")
print(sum(x)/float(len(x)))

print("\nStandard Deviation of generated random numbers:")
print(np.std(x))

print("\nVariance of generated random numbers:")
print(np.var(x))

plt.hist(x,bins=20)
plt.title("Generated Random Numbers")
plt.xlabel("Value")
plt.ylabel("Frequency")

plt.show()

################## End of Question 2 ################## 