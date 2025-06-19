#!/usr/bin/python3

#Ascii border icons: ╔  ╗  ╚  ╝  ╠  ╣  ╟  ╢  ═  ║  ╦  ╩  ╤  ╧  │  ━

#╔════╤════╤════╤════╤════╤════╤════╗
#║ 33 │  3 │    │    │    │    │    ║
#╚════╧════╧════╧════╧════╧════╧════╝

import random
from datetime import datetime
from time import sleep

now = datetime.now()

epoch_time = now.timestamp()
rseed = (epoch_time)
random.seed(rseed)
print ("Random Seed is epoch time: " + str(rseed))

lotto_array = []
num_games = input("How many games? : ")

num_games = int(num_games)

for x in range(num_games):
    now = datetime.now()
    epoch_time=now.timestamp()
    random.seed=epoch_time
    print(epoch_time)
    for y in range(6):
        ball_num = random.randint(1,45)
        while ball_num in lotto_array:
            ball_num = random.randint(1,45)
        lotto_array.append(ball_num)

    print ("Game " + str(x+1))

    print("╔════╤════╤════╤════╤════╤════╗\n║", end="")
    
    for z in range(6):
        if z > 0:
            print("│", end="")
        if len(str(sorted(lotto_array)[z])) == 1:
            print("  " + str(sorted(lotto_array)[z]) + " ", end="")
        else:
            print(" " + str(sorted(lotto_array)[z]) + " ", end="")
    
    print("║")

    print("╚════╧════╧════╧════╧════╧════╝")
    #print (sorted(lotto_array)) ## Printed after sorting lowest to highest

    sleep(1.75)

    lotto_array = []

