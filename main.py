'''
1 for snake
-1 for water 
0 for gun
'''
import random

# Generate a random number from -1, 0, or 1
computer = random.choice([-1, 0, 1])
me = input("Enter your choice (s,w,g) : ").lower()
dict = {"s": 1 , "w":-1 , "g" : 0}
reverse_dict = {1:"snake",-1:"water",0:"gun"}

num = dict[me]
print(f"You chose {reverse_dict[num]} \nComputer chose {reverse_dict[computer]}")

if(computer == num):
    print("It's a Draw..")
elif(computer ==1 and num ==0 ):
    print("You Win")
elif(computer ==1 and num ==-1):
    print("You Lose ")
elif(computer == -1 and num == 0):
    print("You Lose ")            
elif(computer == -1 and num == 1):
    print("You Win")            
elif(computer == 0 and num == 1):  
    print("You Lose ")          
elif(computer == 0 and num == -1): 
    print("You Win")           
else:
    print("Error...")