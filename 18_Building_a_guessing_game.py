secret_word = "steak"; guess = ""; i = 1
while  i <= 5 :
    guess = input("guess: ")
    if guess == secret_word: print("Correct!"); break
    elif guess != secret_word: i += 1
