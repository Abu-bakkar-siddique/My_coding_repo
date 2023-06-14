import random
x =int(input("enter a number between 1 and 100 : ")) 
rand = random.randint (1,x)
guess = 0
while rand != guess :
        guess =int (input("enter a number : "))
        if guess > rand :
                print ("too high try again ")
        elif  guess < rand :
                print ("nope! too low try again ")

print ("yahoo ! you guessed it right")                               

        