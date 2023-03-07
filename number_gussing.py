import random
top_of_range=input("type a number :")#10
if top_of_range.indigit():
       top_of_range=int(top_of_range)
       if top_of_range<=0:
              print("please type a number 0 next time")
              quit()
else:
       print("please type a number next time.")  
       quit()  
random_number=random.randint(0,top_of_range)#5
guesses=0
while true:
       guesses+=1
       user_gusess=input("make a gusess:")#3
       if user_gusess.indigit():
              user_gusess=int(user_gusess)
else:
       print("please enter the number next time") 
       continue
       if user_gusess == random_number:
              print("you got it!!!")
              breat

       

               