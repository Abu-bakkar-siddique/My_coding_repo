import random
import string 
#selecting a word
word = ["python", "code", "hangman", "computer", "program", "algorithm", "variable", "function", 
"loop", "string",    "integer", "list",
 "dictionary", "tuple", "module", "package", "debugging", "conditional", "statement",
    "class", "object", "inheritance", "polymorphism", "encapsulation",
     "exception", "file", "input", "output","recursion", "sorting", "searching", "binary", "decimal", "arithmetic", 
     "boolean", "operator", "comparison",
         "assignment", "random", "import", "print", "return", "break",
      "continue", "while", "for", "if", "else", "elif",    "none"]
SecretWord = random.choice(word)
Used_Letter = ""
var = ""
English_alphabets = string.ascii_letters
n = 10

#getting input
while n > 0 :

    User_typed_letter = input (
        " enter a letter : "
        )
    if User_typed_letter in English_alphabets :

        Used_Letter = Used_Letter + User_typed_letter 

        print (" you have used the folowing letters " , Used_Letter , end = " ")
        print ()
    else :
          print (" please enter a valid character ")  
     
#checking user input
    """if User_typed_letter  in SecretWord  :
        print ("correct !")
                    
    else :
        print(f" wrong !. turns remaining : {n}")
        print ( )"""
    """if User_typed_letter  in SecretWord :
        continue
    else:
        print ("Wrong Guess")
        n = n - 1 
        print(f" wrong !. turns remaining : {n}")"""
        
    for letter in SecretWord :
        dash =  "_" * len(SecretWord)
        print (dash) 
        if letter in Used_Letter :
            
            idx = SecretWord.index(letter)
            #converting the dash variable to a list
            dash_list = list(dash)
            dash_list[idx] = letter
            dash_str = "".join(dash_list)
            print(dash_str, end = " ")
            print ("correct guess")
        else :
            print("Wrong Guess")
            n = n - 1
            print(f"chances remaining {n}")
    
    if  "_" not in dash:
        print(f" yes the word was {SecretWord} \n" )

        print ("you won !")
        break                
    elif n == 0 :
        print ("you lost ") 
        break               