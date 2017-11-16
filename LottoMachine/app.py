'''
Let Python draw 6 numbers for you! Maybe that will be your lucky numbers.
Author: Maciej Tarach
'''

import random

class LottoMachine:
    '''
    Class that simulate the lotto machine.
    numbers - all numbers from 1 to 49 which machine will be drawing.
    result - the 6 numbers randomized from numbers variable
    '''
    #init
    def __init__(self):
        self.numbers = []
        self.result = []

    #fill the numbers
    def fill(self):
        for x in range(1, 50):
            self.numbers.append(x)

    #get 6 numbers
    def randomize(self):
        for num in range(6):
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
