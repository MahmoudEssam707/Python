import random, math
print("""Welcome to our little game \"Guess the number!!\" 
Firstly, you will put your ranges.""")
A = int(input("Please sir put your start range : "))  # here will assign the start of the interval
B = int(input("Please sir put your end range : "))  # here will assign the end of the interval
guess = random.randint(A, B)  # Generating the specific number we need to guess
NOG = round(math.log(B - A + 1, 2))  # this algorithm to calculate the minimum number of guessing depends upon the range
print(f"""Now let's play
Please remember that you have only {NOG} tries !""")
counter = 0  # if this Variable become greater than NOG, then user have done all his tries
while counter < NOG:
    counter += 1
    UserGuess = int(input("your number : "))  # user number
    if UserGuess == guess:
        print("Congratulations You have done it !")
        break
    elif UserGuess < guess and (NOG - counter) != 0:
        print(f"Take care ! your number is Smaller than it, You have only {NOG - counter}")
    elif UserGuess > guess and (NOG - counter) != 0:
        print(f"Take care ! your number is Greater than it, You have only {NOG - counter}")
if counter >= NOG:
    print(f"""I know it's sad but you have done all your tries and the number was : {guess}
Don't worry,Best luck next time !!""")