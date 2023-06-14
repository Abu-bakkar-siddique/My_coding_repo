import random 
up =  int (input ("what's the upper limit :"))
do = int (input ("what's the lower limit :"))
x = random.randint (do,up)
feedback = (" ")
while feedback != ("correct") :
    
    feedback = input (f" is {x}  correct ? ")
    if feedback == "lower" :
        x = x - 1
    elif feedback == "higher" :
        x = x + 1
    elif feedback == "correct" :

        print ( "yes ! you guessed it right ")   
              
        