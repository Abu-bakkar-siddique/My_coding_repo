#Mealtime

def convert (Time) :
    Time = Time.replace (".","")
    am_pm = Time[-2:]
    if am_pm == "am" or am_pm == "pm" :
        hours , mins = Time.split(":")
        min,Am_Pm = mins.lstrip().split(" ")
        dec_hrs = float(hours) + float(min)/60
        return dec_hrs 
    else :
        hours , mins = Time.split (":")
        dec_hrs = float (float(hours)+float(mins)/60)
        return dec_hrs
        
def main () :
    Time = input("what time is it? ")
    time = convert (Time)
    if (8 >= time >= 7)  or  ((8 >= time >= 7) and ("am" in Time)) :
        print("breakfast time")
    elif ((13 >= time >= 12) or ((13 > time >= 12)) and ("pm" in Time) ) or time == 1.0 :
        print ("lunch time")
    elif ((19 >= time >= 18) or ((7 >= time >= 6))  and ("pm" in Time)) :
        print ("dinner time")
    else :
        print (" ")
if __name__ == "__main__" :
    main ()