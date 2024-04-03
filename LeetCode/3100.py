#class Solution:
    #def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        
        # numBottles : the number of full water bottles that I initially have
        # numExchange : the limit that I can exchange for full bottles
        # emptyBottle : the number of empty bottles
        # exchange_time : how many times that I exchange EB to FB
        
        #emptyBottle = 0

        #total = numBottles

        #emptyBottle = numBottles

        #exchange_time = 0

        #while emptyBottle >= numExchange :

            #emptyBottle = emptyBottle - numExchange
            #numExchange = numExchange + 1
            #numBottles = numBottles + 1 
        
        
        #total = total + numBottles

        #return total
    



class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:

        total, emptyBottles = numBottles, numBottles

        while emptyBottles >= numExchange:
            emptyBottles = emptyBottles - numExchange + 1 # got the 
            numExchange = numExchange + 1
            total = total + 1

        return total
        