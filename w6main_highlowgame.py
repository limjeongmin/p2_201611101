def highlowgame():
    import random
    guessesTaken = 0
    print("Hi!, what is your name?") 
    myName = input()
      
    number = random.randint(1,200)
    print('well, '+ myName + ', I am thinking of a number 1 and 200.')
    while guessesTaken < 10:
        print ('Taken a guess')
        guess = input()
        guess = int(guess)
        
        guessesTaken = guessesTaken + 1
        if guess < number:
            print ('Your guess is too low')
        if guess > number:
            print ('Your guess is too high')
        if guess == number:
            print ('That is right')
            break
    if guess == number:
        guessesTaken = str(guessesTaken)
        print ('Great, ' + myName + '! You guessed my number in' + guess-Taken +'guesses!')
    
    if guess != number:
        number = str(number)
        print ('Nope. The number I was thinking of was ' + number)

highlowgame()
wn.exitonclick()

"""
@startuml 
title UpDownGame 
start  
:Select random one number in range; 
:Try to guess the number; 
:Player input one number;  
while(Play) 
if (Compare Player number & answer) then (Player number < answer) 
:high; 
else (Player number > answer) 
:low; 
endif 
endwhile 
:Player number = answer; 
:You win; 
:End Game; 
stop 
@enduml
""" 

def lab6():
	highlowgame()

def main():
	lab6()

if __name__=="__main__":
	main()