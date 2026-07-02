#roll the dice

import random

while True:
    print(" Do you want to roll the dice? Y/N")
    user_choice=input().lower()

    if user_choice=='y':
       first_num=random.randint(1,6)
       second_num=random.randint(1,6)
       print (f"[{first_num},{second_num}]")

    elif user_choice=='n':
       print("Hope you have a good day")
    else:
       print ("Sorry I don't understand")

