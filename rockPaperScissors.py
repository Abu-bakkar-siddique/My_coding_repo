import random
while True :
    try :
        
        print('\n')
        print ("Hi,select p for paper , r for rock , s for scissors :)")
        print ()
        user_choice = str  (input ("enter a character : "))
    except   :

        print ("please enter a valid character ")
    else :    
        computer_choice = random.choice (['r','p','s']) 

    
    #tie condition 
        if user_choice == computer_choice :
            print ("its a tie\n")
    
    #win conditions
        elif user_choice == "r" and computer_choice == "s" :
            print ("you win !")

        elif user_choice == "p" and computer_choice == "r" :
            print ("you win !")

        elif user_choice == "s" and computer_choice == "p" :
            print ("you win !")

    #lose conditions
        elif user_choice == "r" and computer_choice == "s" :
            print ("you lose \n")

        elif user_choice == "S" and computer_choice == "r" :
            print ("you lose \n")

        elif user_choice == "p" and computer_choice == "s" :         
            print ("you lose \n")
