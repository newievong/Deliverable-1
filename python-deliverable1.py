name = input("Welcome to GC mini golf! What is your name?")
num_of_holes = int(input(f"Hi,{name}! Would you like to play 3 or 6 holes?"))

if num_of_holes == 3:
    hole1 = int(input("How many putts for hole 1? (Par: 3)"))
    hole2 = int(input("How many putts for hole 2? (Par: 3)"))
    hole3 = int(input("How many putts for hole 3? (Pur: 3)"))

    total_score = int(hole1 + hole2 + hole3 - 9)
    if total_score == 0:
        print(f"Good game, {name}! Your total score was: 0")
    elif 0 < total_score > 9:
        print(f"Nice try {name}. Your total score was: +{total_score}")
    else:
        print(f"Great job, {name}! Your total score was: {total_score}.")
else:
    hole1 = int(input("How many putts for hole 1? (Par: 3)"))
    hole2 = int(input("How many putts for hole 2? (Par: 3)"))
    hole3 = int(input("How many putts for hole 3? (Pur: 3)"))
    hole4 = int(input("How many putts for hole 4? (Par: 3)"))
    hole5 = int(input("How many putts for hole 5? (Par: 3)"))
    hole6 = int(input("How many putts for hole 6? (Pur: 3)"))

    total_score = int((hole1 + hole2 + hole3 + hole4 + hole5 + hole6) - 18)
    if total_score == 0:
        print(f"Good game, {name}. Your total score was: 0.")
    elif 0 < total_score > 18:
        print(f"Nice try, {name}... Your total score was: +{total_score}")
    else:
        print(f"Great job, {name}! Your total score was: {total_score}.")







