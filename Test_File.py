import string
word = "hello"
dash = ["_"]*len(word)
used_letters = ""
valids = string.ascii_letters
n = 10
while n > 0:
    user_letter = input("Enter a letter: ")
    # validating the user input 
    if user_letter == "" or len(user_letter) > 1 or user_letter not in valids:
        print ("please Enter a letter at a time.")
        continue
    
    if user_letter not in word:
        n = n - 1
        print("wrong guess!\n", end = " ")
        print (f"Guesses left:{n}")
    else:
        print("correct guess", end = " ")    
    used_letters = used_letters + user_letter
    for i,letter in enumerate(word):
        if letter in used_letters :
          
            dash = list(dash)
            dash[i] = letter
            dash = "".join(dash)
    
    print("".join(dash))
    if "_" not in dash:
        print("Yes! You guessed it right")
        break