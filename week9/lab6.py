##############################
# APS106 Winter 2022 - Lab 6 #
##############################

import random
from itertools import combinations

#####################################
# HELPER FUNCTIONS TO HELP PLAY THE
# GAME - NO NEED TO EDIT THESE
#####################################

def generate_deck():
    """
    (None) -> [[suit, number],[suit,number], ...]

    Create a standard deck of cards with which to play our game.
    Suits are: spades, clubs, diamonds, hearts
    Numbers are: 1 -13 where the numbers represent the following cards:
        1  - Ace
        11 - Jack
        12 - Queen
        13 - King
        2-10 - Number cards
    """

    deck = []
    suits = ['spades','clubs','diamonds','hearts']

    for suit in suits:
        for number in range(1,14):
            deck.append([suit,number])

    return deck

def shuffle(deck):
    """
    (list) -> list

    Produce a shuffled version of a deck of cards. This should shuffle a deck
    containing any positive number of cards.

    Note, this function should return a new list containing the shuffled deck
    and not directly reorder the elements in the input list. That is, the
    list contained in 'deck' should be unchanged after the function returns.
    """

    shuffled_deck = random.sample(deck,len(deck))

    return shuffled_deck

#############################
# PART 1 - Deal card
#############################

def deal_card(deck,hand):
    """
    (list,list) -> None

    Deal a card from the first element in the deck list and add it to the list
    representing the player's hand. Both list input parameters
    are nested lists with each element in the list being a two-element
    list representing a card.
    
    Note that this function returns nothing! It modifies the two lists that 
    are passed in as parameters in place.

    """
    # TODO your code here    
    hand.append(deck.pop(0))
    #print(deck)
    #print(hand)


#deal_card([['spades', 10], ['hearts', 2], ['clubs', 8]], [['diamonds', 3]])

'''
from itertools import combinations
lst = ["1h","2s","2d","3h","3s"]
combos_of_two = list(combinations(lst, 2)) # returns list of all n choose 2 combinations
combos_of_three = list(combinations(lst, 3)) # returns list of all n choose 3 combinations
print(combos_of_three)
#print(combos_of_two)

'''
#############################
# PART 2 - Score Hand
#############################

from itertools import combinations

def score_hand(hand):
    """
    (list) -> int

    Calculate the cribbage score for a hand of five cards. The input parameter
    is a nested list of length 5 with each element being a two-element list
    representing a card. The first element for each card is a string defining
    the suit of the card and the second element is an int representing the 
    number of the card.
    """
    
    # TODO your code here
    totalPointsFromRule1 = 0

    combosOfTwo = list(combinations(hand,2))
    combosOfThree = list(combinations(hand,3))
    combosOfFour = list(combinations(hand,4))


    for combination in combosOfTwo:
        if combination[0][1] == combination[1][1]:
            totalPointsFromRule1 += 2
    
    #print("rule 1",totalPointsFromRule1)
    
    totalPointsForRule2 = 0
    '''
    rule2Counter = 0
    firstSuit = hand[0][0]
    for suit in hand:
        if suit[0] == firstSuit:
            rule2Counter += 1
    
    if rule2Counter == 4:
        totalPointsForRule2 += 4
       
    if rule2Counter == 5:
        totalPointsForRule2 += 5
    '''
    suitsDic = {'diamonds':0, 'hearts':0, 'clubs':0, 'spades':0}
    for card in hand:
        card = card[0]
        currentValue = suitsDic.get(card) + 1

        suitsDic.update({card : currentValue})
        
    
    #print(suitsDic)
    for suits in suitsDic:
        if suitsDic.get(suits) == 5:
            totalPointsForRule2 += 5
        if suitsDic.get(suits) == 4:
            totalPointsForRule2 += 4
    
    #print("rule 2",totalPointsForRule2)

    rule3Counter = 0
    #all card numbers in the hand
    cardNum = set()
    for card in hand:
        cardNum.add(card[1])
        
    #print(cardNum)
    #all runs possible with 5 cards
    combos = []
    for i in range(1,10):
        tempSet = set([i,i+1,i+2,i+3,i+4])
        combos.append(tempSet)
    
    #print(combos)
    for combo in combos:
        if len(combo.difference(cardNum)) == 0:
            rule3Counter += 5
    
    #print("rule 3 A", rule3Counter)
    
    if rule3Counter < 5:
        combos = []
        for i in range(1,11):
            tempSet = set([i,i+1,i+2,i+3])
            combos.append(tempSet)

        #print(combos)
        combosOfFourNum = []
        for handCombo in combosOfFour:
            tempSet = set()
            for num in handCombo:
                tempSet.add(num[1])
            combosOfFourNum.append(tempSet)

        for setCombo in combosOfFourNum:
            if len(setCombo) == 4:
                for combo in combos:
                    if len(combo.difference(setCombo)) == 0:
                        rule3Counter += 4
                        
        #print("rule 3 B", rule3Counter)
        
    if rule3Counter < 4:
        combos = []
        for i in range(1,12):
            tempSet = set([i,i+1,i+2])
            combos.append(tempSet)
        #print("combos",combos)
        
        combosOfThreeNum = []
        for handCombo in combosOfThree:
            tempSet = set()
            for num in handCombo:
                tempSet.add(num[1])
            combosOfThreeNum.append(tempSet)
        #print(combosOfThreeNum)

        for setCombo in combosOfThreeNum:
            if len(setCombo) == 3:
                for combo in combos:
                    if len(combo.difference(setCombo)) == 0:
                        rule3Counter += 3
                        
        #print("rule 3 C", rule3Counter)
    
    rule4Counter = 0
    
    allCombos = []
    
    for handCombo in combosOfTwo:
        tempSet = []
        for num in handCombo:
            if num[1] > 10:
                tempSet.append(10)
            else:
                tempSet.append(num[1])
        allCombos.append(tempSet)
        
    for handCombo in combosOfThree:
        tempSet = []
        for num in handCombo:
            if num[1] > 10:
                tempSet.append(10)
            else:
                tempSet.append(num[1])
        allCombos.append(tempSet)
        
    for handCombo in combosOfFour:
        tempSet = []
        for num in handCombo:
            if num[1] > 10:
                tempSet.append(10)
            else:
                tempSet.append(num[1])
        allCombos.append(tempSet)

    tempSet = []
    for num in hand:
        if num[1] > 10:
                tempSet.append(10)
        else:
            tempSet.append(num[1])
    allCombos.append(tempSet)
    
    for combo in allCombos:
        if sum(combo) == 15:
            rule4Counter += 2
    
    #print("rule4", rule4Counter)
    
    finalCounter = totalPointsFromRule1 + totalPointsForRule2 + rule3Counter + rule4Counter
    
    #print("final", finalCounter)
    return finalCounter
#deal_card([['spades', 10], ['hearts', 2], ['clubs', 8]], [['diamonds', 3]])
 
hand1 = [['spades', 3], ['diamonds', 4], ['diamonds', 5], ['diamonds', 6], ['diamonds', 9]]

score_hand(hand1)


################################
# PART 3 - PLAY
################################

def play(shuffled_deck):
    """
    (list) -> [str, int, int]
    
    Function deals cards to players, computes player scores, and
    determines winner.
    
    Function retuns a three-element list where the first element is a string
    indicating the winner, the second element is an int specifying player\'s
    score, and the third element is an int specifying dealer\'s score.
    """
    player_hand = []
    dealer_hand = []
    
    # TODO complete the function

    for num in range(1,12):
        if num % 2 != 0:
            deal_card(shuffled_deck, dealer_hand)
        else:
            deal_card(shuffled_deck, player_hand)
    
    player_score = score_hand(player_hand)
    dealer_score = score_hand(dealer_hand)
    
    if player_score > dealer_score:
        return ["player wins", player_score, dealer_score]
    else:
        return ["dealer wins", player_score, dealer_score]
