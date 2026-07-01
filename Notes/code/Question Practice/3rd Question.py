secret_number = 7
while True:
    guess = int(input("Guess a number between 1 and 9: "))
    if guess == secret_number:
        print("Well guessed!")
        break
    else:
        print("Try again!")