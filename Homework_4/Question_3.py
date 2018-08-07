# Brian Powell 012362894
# EE381 - Chaw-Long Chu
#
# Homework_4
#
# Question_3
# A quality control unit inspects 400 poieces products every day. 35 of the products have defects, what is the highest number of defective products that will be found? 
# And what is the probability?
#

import matplotlib
from scipy.stats import binom

print("Homework_4")
print("Question_1")
n = 400
p = .03
k = 12
y = binom.pmf(k,n,p)
print("\nHighest number of defective products found:")
print(k)
print("\nProbability of finding " + str(k) + " defective products:")
print(y)

