def main () :
    MealCost = input ("how much was the meal  : ")
    tipPercentage = input ("what percentage you want to leave for tip : ")

    Dollar = dollars_to_float(MealCost)
    Percentage = percent_to_float(tipPercentage)

    tip = (Percentage * Dollar ) / 100

    print (f"leave ${tip :.2f} .")


def dollars_to_float(d):
    d = d.replace("$" , "")
    d = float (d)

    return d

def percent_to_float(p):
    p = p.replace("%" , "")
    p = float(p)
    return p 

main ()











