# Brian Powell 012362894
# EE 381 - Dr. Chaw-Long Chu
# Homework #1
# 
#Question 3: An ordinary deck of playing cards (52 cards, 4 suits and 13 ranks) is shuffled, and one card is randomly chosen 
#(all cards are equallyt likely).
#A. What is the prbability to have a Queen?
#B. If 2 cards are randomly chosen, what is the probability to have one Queen and one Diamond?
#

QueenProbability = float(4/52)
DiamondProbability = float(13/51)

#A
print("Probability to draw one Queen out of an ordinary deck of 52 cards: ", QueenProbability)

#B
QueenAndDiamondProbability = float(QueenProbability * DiamondProbability)
print("Probability to draw a Queen and Diamond: ", QueenAndDiamondProbability)

################## End of Question 3 ################## 