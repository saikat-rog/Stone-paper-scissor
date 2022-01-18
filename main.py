import random
print("WELCOME!! to our Stone, paper, siezer game.\n.............................................")
rand = random.randint(1,3)
if rand == 1:
    randstr = "STONE"
if rand == 2:
    randstr = "PAPER"
if rand == 3:
    randstr ="SIEZER"


user_turn = input("Choose(Stone, Paper or siezer): ")
user_turn_upper = user_turn.upper()
print(user_turn_upper)
print("\n")
user_rand = 0
if user_turn.lower() == "stone":
    user_rand = 1
if user_turn.lower() == "paper":
    user_rand = 2
if user_turn.lower() == "siezer":
    user_rand = 3

# print(user_rand)
# print(rand)


if rand == user_rand:
    print(f"Computer is: {randstr} and you are also: {user_turn_upper}. So,Draw!! Play again.\n\n")

if rand == 1 and user_rand == 3:
    print(f"Computer is: {randstr} and you are: {user_turn_upper}. So,Computer own.\n\n")
if rand == 3 and user_rand == 1:
    print(f"Computer is: {randstr} and you are: {user_turn_upper}. So,You own.\n\n")

if rand == 1 and user_rand == 2:
    print(f"Computer is: {randstr} and you are: {user_turn_upper}. So,You own.\n\n")
if rand == 2 and user_rand == 1:
    print(f"Computer is: {randstr} and you are: {user_turn_upper}. So,Computer own.\n\n")

if rand == 2 and user_rand == 3:
    print(f"Computer is: {randstr} and you are: {user_turn_upper}. So,You own.\n\n")
if rand == 3 and user_rand == 2:
    print(f"Computer is: {randstr} and you are: {user_turn_upper}. So,Computer own.\n\n")

