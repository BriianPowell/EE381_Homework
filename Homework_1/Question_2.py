# Brian Powell 012362894
# EE 381 - Dr. Chaw-Long Chu
# Homework #1
#
# Question 2: If you throw a fair die 10 times, which has six sides marked numbers from 1 to 6, how many times you may
# have '1'? Find a different throwing number to have the probablility to have '1' to be 1/6 (use random number to work 
# to prove your answer).
#

import random

def dice_roll():
    rollcount = int(input("How many times would you like to roll?"))
    testcount = 0

    for i in range(0, rollcount):
        roll_num = random.randint(1,6)
        if roll_num == 1:
            testcount += 1
            print(str(roll_num))
        else:
            print(str(roll_num))

    print("You rolled a 1 [", testcount, "] time(s).")
    ratio = float(testcount / rollcount)
    print("You're probably ratio is of finding a 1 is: ", ratio) 

def main():
    game_start = input("Would you like to roll a dice? ")
    if game_start == "yes":
        dice_roll()
    else:
        print("Exit.")

if __name__ == '__main__':
    main()

################## End of Question 2 ##################