import random 

def ComputerGuess(x):
    low= 0
    high = x
    feedbck = ""
    while feedbck != 'c':
        if low != high:
            guess  = random.randint(low,high)
        else:
             guess = low
        
        feedbck = input(f'Is {guess}  too hight(H),too low(L) or correct(C)?').lower()
        if feedbck == 'h':
                high = guess -1 
        elif feedbck == 'l':
                low = guess + 1
    print(f'yay,the computer have guessed your number is {guess} , Correctly')

          


ComputerGuess(100)



