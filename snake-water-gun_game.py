import random
def game(comp,you):


 if comp==you:
        
        return None
 elif comp=="s":
        if you=="p":
            return True
        elif you=="w":
           return False
 elif comp=="p":
        if you=="w":
            return True
        elif you=="s":
            return False
 elif comp=="w":
        if you=="s":
            return True
        elif you=="p":
            return False                 
print("COMPUTER TURN :  STONE(s), PAPER(p), SCISSORS(w)")                
randno=random.randint(1,3)
if randno==1:
    comp='s'
if randno==2:
    comp='p'
if randno==3:
    comp='w'       
you= input("YOUR TURN :  STONE(s), PAPER(p), SCISSORS(w)")       
print(" computer choose :"   + (comp))
print(" you choose :"   + you)
l = game (comp,you)
if l==None :
    print("THIS IS A TIE")
elif l:
    print("YOU WIN")
else:
    print(" YOU LOSE ")
''' print("this is my first game")        '''       