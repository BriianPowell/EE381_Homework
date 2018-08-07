# Brian Powell 012362894
# EE 381 - Dr. Chaw-Long Chu
# Homework #1
# 
# Question 1: A group of boy students has heights (in inches) as (65,67,72.5,71,82,59,62,63.4,66,65,73,71,72)
# and girl students has heights (in inches) as (58,56.5,54,60,62,59,60.5,61,63,65,66,61.5,62.5). Please use 
# histogram (bins = 5) to represent these dat ain one graph. Legend, x, y coordinates, and title are needed
# for the graph.
#

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
boy = [65,67,72.5,71,82,59,62,63.4,66,65,73,71,72]
girl = [58,56.5,54,60,62,59,60.5,61,63,65,66,61.5,62.5]

bin_edges = 5

plt.hist([boy, girl], bins=bin_edges, histtype='bar', rwidth=0.8, color=['green','cyan'],
            label=["Boys", "Girls"])

plt.title("Distrubution of Boys and Girls Height in Inches")
plt.ylabel("Height (in inches)")
plt.xlabel("Height Distribution")
plt.legend()
plt.show()

################## End one Question 1 ##################