import string
import sys
import random
alpha = string.ascii_letters
dig = string.digits
punc = string.punctuation
def validating_len():

    try:
     l_en = int(input("Enter password length: "))
    except ValueError:
        sys.exit("please enter valid length")
    return l_en

def check_length(l):
    if l % 2 == 0:
        return int(l//3)
    else:
        q, r = divmod(l,3)
        return [int(q),int(r)]

def generate_password (q, r = 0):
    letters = random.sample(alpha, q)
    #letters = letters

    punctuations = random.sample(punc, q)
    #punctuations = punctuations

    numbers = random.sample(dig, q)
    #numbers = numbers
    spaces = random.sample(range(q), r)
    string = f"{''.join(letters)}{''.join(numbers)}{''.join(punctuations)}"
    for i in spaces:
        string = string[:i]+" "+string[i:]
    return string    

def main():

    l = validating_len()
    lst = check_length(l)
    if isinstance(lst, list):        
        print (generate_password (lst[0], lst[1]))
    else:
        print (generate_password (lst)) 

if __name__ == "__main__" :
    main()
