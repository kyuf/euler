#euler 54
"""
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
"""
class Player:    
    def new_hand(self, hand):
        self.hand = hand
        self.values = [0] * 13
        self.suits = {}
        self.high = {1: [], 2: [], 3: [], 4: []}
        
        #baseline rank of 1 (high card)
        self.rank = 1
        
        for card in hand:
            #holding value and suit of current card
            value = card[0]
            suit = card[1]
            
            #store values of cards
            if value == "A":
                self.values[12] += 1
            elif value == "K":
                self.values[11] += 1
            elif value == "Q":
                self.values[10] += 1
            elif value == "J":
                self.values[9] += 1
            elif value == "T":
                self.values[8] += 1
            else:
                self.values[int(value) - 2] += 1
    
            #store suits of cards
            if suit in self.suits:
                self.suits[suit] += 1
            else:
                self.suits[suit] = 1
        
        #store high values of cards
        for i in range(13):
            if self.values[i] > 0:
                self.high[self.values[i]].append(i)
        
        #run checks
        self.check_kinds()
        
        #only run if no kinds found
        if self.rank == 1:
            self.check_straight()
            self.check_flush()
        
    def __repr__(self):
        show_hand = ""
        for i in self.hand:
            show_hand += (i + " ")
        return show_hand
    
    #check if hand is flush
    def check_flush(self):
    
        #only 1 suit if flush
        if len(self.suits) == 1:
            self.is_flush = True
        else:
            self.is_flush = False
        
        #check flush/straight combinations (including royal)
        if self.is_flush:
            if self.is_royal:
                #royal flush
                self.rank = 10
            elif self.is_straight:
                #straight flush
                self.rank = 9
            else:
                #flush
                self.rank = 6
    
    #check if hand is straight
    def check_straight(self):
        started = False
        consecutive = 0
        self.is_royal = False
        self.is_straight = False
        
        #modulus needed for ace wrap around
        for i in [j % 13 for j in range(12, 26)]:
        
            #first card has been found
            if started:
            
                #increment consecutive for each consecutive card
                if self.values[i] == 1:
                    consecutive += 1
                else:
                
                    #is straight if consecutive == 5 on termination
                    if consecutive == 5:
                        self.is_straight = True
                        #straight
                        self.rank = 5
                        
                    #royal straight possibility
                    elif i == 0:
                        started = False
                        consecutive = 0
                        continue                       
                    return
                    
            #first card has not been found yet
            else:
            
                #not straight if hand has duplicate values or jack first card
                if self.values[i] > 1 or i == 9:
                    return
                    
                #first card
                elif self.values[i] == 1:
                    started = True
                    consecutive += 1
        
        #complete loop means straight is royal
        self.is_royal = True
        
        #lowest possible rank is straight
        self.is_straight = True
        self.rank = 5
    
    #check for pairs, 3 of a kind, full house, 4 of a kind, high card
    def check_kinds(self):
        if self.high[4]:
            #4 of a kind
            self.rank = 8
        elif self.high[3]:
            if self.high[2]:
                #full house
                self.rank = 7
            else:
                #3 of a kind
                self.rank = 4
        elif self.high[2]:
            if len(self.high[2]) == 2:
                #two pair
                self.rank = 3
            else:
                #pair
                self.rank = 2
    
    #compare high cards when tie
    def compare_high(self, other, h):
        while self.high[h]:
            #set current high value
            p1 = self.high[h].pop()
            p2 = other.high[h].pop()
            
            if p1 > p2:
                return 1
            elif p1 < p2:
                return 0
        
        #in case of tied values
        if h == 7:
            return self.compare_high(other, 2)
        else:
            return self.compare_high(other, 1)
                
    #return 1 if self beats other else 0
    def vs(self, other):
        if self.rank > other.rank:
            return 1
        elif self.rank < other.rank:
            return 0
        else:
            #check high ones
            if self.rank in {1, 5, 6, 9}:
                return self.compare_high(other, 1)
            #check high twos
            elif self.rank in {2, 3}:
                return self.compare_high(other, 2)
            #check high threes
            elif self.rank in {4, 7}:
                return self.compare_high(other, 3)
            #check high fours
            else:
                return self.compare_high(other, 4)
                
player1 = Player()
player2 = Player()

p1_wins = 0

with open("poker.txt", "r") as f:
    for line in f:
        #remove \n and spaces in each line
        cards = line.rstrip().split(" ")
        
        #assign cards to players
        player1.new_hand(cards[:5])
        player2.new_hand(cards[5:])
        
        """
        print("Player 1: ", player1)
        print("Player 2: ", player2)
        """
        
        #track outcome
        p1_wins += player1.vs(player2)

print(p1_wins)

"""
test = Player()
test.new_hand(["3S", "2H", "6C", "4D", "AC"])
print(test.rank)
"""
