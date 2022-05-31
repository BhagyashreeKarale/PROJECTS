#PROBLEM
'''
You are a Pokémon trainer. Each Pokémon has its own power, described by a
positive integer value. As you travel, you watch Pokémon and you catch each of
them. After each catch, you have to display maximum and minimum powers of
Pokémon caught so far. You must have linear time complexity. So sorting won’t
help here. Try having minimum extra space complexity.
'''

#SOLUTION
def pokemonTraining(powersList):    
    for i in range(len(powersList)):
        powersCaughtSoFar=powersList[:i+1]
        print(min(powersCaughtSoFar),max(powersCaughtSoFar))
