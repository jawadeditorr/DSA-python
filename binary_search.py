"""
QUESTION 1: Alice has some cards with numbers 
written on them. She arranges the cards in decreasing 
order, and lays them out face down in a sequence on a 
table. She challenges Bob to pick out the card 
containing a given number by turning over as few cards 
as possible. Write a function to help Bob locate the card.
"""

cards = [13,11,10,6,4,3,1,0]

def binary_search(cards,query,mid):

    if cards[mid]==query and mid<len(cards):
        return mid
    elif cards[mid]>query and mid<len(cards):
        mid = mid + mid//2
        return binary_search(cards,query,mid)
    elif cards[mid]<query and mid<len(cards):
        mid = mid//2
        return binary_search(cards,query,mid)
    else:
        return -1

def locate_card(cards,query):
    mid = len(cards)//2
    return binary_search(cards,query,mid)

print(locate_card(cards,11))