import random

               #r for rock p for paper and s for scissor
ask = str (input ("enter your choice as r , p , s : ") )
               
z = random.choice (["r" , "p" , "s"])
print  (f"the computer chose {z}")
print ()

if ask == z :
    print ("it's a tie")

elif ask =="r" and z == "s" or ask == "s" and z == "p" or ask == "p" and z == "r" :
    print ("yahoo you won ")
    print( )
else :
        print ( "you lost" ) 
        print ()


   


