# Brian Powell 012362894
# EE381 - Chaw-Long Chu
#
# Homework_4
#
# Question_1
# Using Binomial Distribution to calculate the probability of getting less than 3 times of "5" in 8 throws of a fair die?
#

import matplotlib
from scipy.stats import binom

print("Homework_4")
print("Question_1")
n = 8
p = 1/6
k = 3
y = binom.pmf(k,n,p)
print("Probability of getting less than 3 times of \"5\" in 8 throws of a fair die:")
print(y)

################## End of Question 1 ################## 