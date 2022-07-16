# Main Question
# Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card.


# Problem Interpreted:
# We need to write a program to find the position of a given number in a list of numbers arranged in decreasing order. We also need to minimize the number of times we access elements from the list.
from jovian.pythondsa import evaluate_test_case


# Brute force Solution
def locate_card(cards,query):
    if len(cards) > 0:
        for position in range(len(cards)):
            if cards[position] == query:
                return position
    return -1

print(locate_card([13,12,11,10,9,8],5))
