#euler 98
"""
By replacing each of the letters in the word CARE with 1, 2, 9, and 6 respectively, we form a square number: 1296 = 362. What is remarkable is that, by using the same digital substitutions, the anagram, RACE, also forms a square number: 9216 = 962. We shall call CARE (and RACE) a square anagram word pair and specify further that leading zeroes are not permitted, neither may a different letter have the same digital value as another letter.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, find all the square anagram word pairs (a palindromic word is NOT considered to be an anagram of itself).

What is the largest square number formed by any member of such a pair?

NOTE: All anagrams formed must be contained in the given text file.
"""
from math import ceil, floor

class Word:
    def __init__(self, word):
        self.letters = {}
        self.has_square = True
        self.word = word
        #store quantity of each letter for anagram comparison
        for i in self.word:
            if i in self.letters:
                self.letters[i] += 1
            else:
                self.letters[i] = 1
                
    def __repr__(self):
        return self.word
    
    #check if n digits match letters in word
    def match(self, n):
        self.check = {}
        #set of digits that have not been assigned yet
        available = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "0"}
        n_str = str(n)
        for i in range(len(self.word)):
            if self.word[i] in self.check:
                if self.check[self.word[i]] != n_str[i]:
                    return False
            else:
                if n_str[i] not in available:
                    return False
                self.check[self.word[i]] = n_str[i]
                available.remove(n_str[i])
        self.n = n
        return True
    
    #check if two words are anagramic squares based on one's letter digits
    def is_pair(self, other):
        new_square = ""
        #starting digit cannot be 0
        if self.check[other.word[0]] == "0":
            return False
        for i in other.word:
            new_square += self.check[i]
        new_square = int(new_square)
        root = int((new_square ** 0.5) + 0.5)
        if root ** 2 == new_square:
            other.n = new_square
            return True
        else:
            return False
            

#returns a list of n-digit squares
def n_digit_square(n):
    N = []
    for i in range(int(ceil(10 ** ((n - 1) / 2))), int(floor(10 ** (n / 2)))):
        N.append(i ** 2)
    return N

with open("words.txt", "r") as f:
    word_list = f.readline().split('","')
    word_list[0] = word_list[0][1:]
    word_list[-1] = word_list[-1][:-2]

word_length_dic = {}

#separate words into groups by length stored in word_length_dic
#key in word_length_dic is the number of letters in word
for i in word_list:
    length = len(i)
    #valid length is > 1
    if length > 1:
        if length in word_length_dic:
            word_length_dic[length].append(Word(i))
        else:
            word_length_dic[length] = [Word(i)]

#maximum word length is 14
#9999999 is the largest number which will produce a 14 digit number

N_values = {"length": 0}
max_n = 0

#find all anagrams by comparing words with same length
for word_length, n_length_words in word_length_dic.items():
    length = len(n_length_words)
    for i in range(length):
        j = i + 1
        while j < length:
            #if two words are anagrams
            if n_length_words[i].letters == n_length_words[j].letters:
                
                #set N_values to contain squares with digits equal word length
                if N_values["length"] != word_length:
                    N_values["length"] = word_length
                    N_values["squares"] = n_digit_square(word_length)
                    
                for n in N_values["squares"]:
                    if n_length_words[i].match(n):
                        if n_length_words[i].is_pair(n_length_words[j]):
                            #output check
                            """
                            print(n_length_words[i].check)
                            print(n_length_words[j].n)
                            """
                            if n_length_words[i].n > max_n:
                                max_n = n_length_words[i].n
                            if n_length_words[j].n > max_n:
                                max_n = n_length_words[j].n
                #output anagram pairs
                """
                print(n_length_words[i], n_length_words[j])
                """
            j += 1
            
print(max_n)
