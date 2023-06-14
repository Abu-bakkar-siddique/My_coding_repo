def board():
     board = [
          "-","-","-",
          "-","-","-",
          "-","-","-"
          ] 

     return board       
def show(x = 0, o = 0):
     B = board ()
     B[x] = "X"
     B[o] = "O"
     
     p=f"""             {B[0]} | {B[1]} | {B[2]}
           +-----+-----+         
             {B[3]} | {B[4]} | {B[5]}          
           +-----+-----+         
             {B[6]} | {B[7]} |  {B[8]}"""
     return p
def decide_turn():
     
     n = 1
     while n != 9:
          if n%2 == 0:
               x = int(input("X chose a  box(0 to 8): "))
               if x<0 or x>8:
                    print("please select valid box")
                    continue
               b[x] = "X"

          else :
               o = int(input("O chose a box(0 to 8): "))
               if o<0 or o>8:
                    print("please select valid box")
                    continue
               #b = board()
               b[o] = "O"
               

          n = n + 1
b = board()          
print(show())          
decide_turn()  

    
          