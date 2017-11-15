'''
Let Python draw 7 numbers for you! Maybe that will be your lucky numbers.
Author: Maciej Tarach
'''

import random

class LottoMachine:
    '''
    Class that simulate the lotto machine.
    numbers - all numbers from 1 to 49 which machine will be drawing.
    result - the 7 numbers randomized from numbers variable
    '''
    #init
    def __init__(self):
        self.numbers = []
        self.result = []

    #fill the numbers
    def fill(self):
        for x in range(1, 50):
            self.numbers.append(x)

    #get 7 numbers
    def randomize(self):
        for num in range(7):
            x = random.choice(self.numbers)
            self.numbers.remove(x)
            self.result.append(x)
            
    #print the result
    def printNumbers(self):
        print(sorted(self.result))

lotto = LottoMachine()
lotto.fill()
lotto.randomize()
lotto.printNumbers()
