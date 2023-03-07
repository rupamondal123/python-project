name= input("type your nsame!")
print("welcome",name,"to this adventure!")
answer=input("you are on a dirt road,it has come to an end you can go left or right.which way would you like to go?").lower()
if answer=="left":
       answer=input("you come to a river,you can walk around it or swim across?type walk to walk around and swim if you want to swimacross:")
       if answer=="swim":
              print("you swam across the river and were eaten by an alligator")
       elif answer=="walk":
              print("you walked miles,ran out of water and lost the game.")  
       else:
              print("not a valid option.you lose") 
elif answer=="right":
       answer=input("you come across a bridge,its looks woobbly,do you want to cross it or head back (cross/back)?")  
       if answer=="back":
              print("you go back and lose")
       elif answer=="cross":
              answer=input("you cross the bridge and met a stranger.Do you want to talk to him (yes/no)")  
              if answer=="yes":
                     print("you talk to the stranger and they gift you the treasure.you won!!!")
              elif answer=="no":
                     print("you ignore the stranger and they get offeneded and you lose") 
              else:
                     print("invalid option you lose")
       else:
              print("invalid option you lose")  
else:
       print("invalid option you lose!!!")  
       print("thank you for trying name",name)            


              



                     


       
