correct_number = 9
guess_count = 0
limit = 3

while guess_count < limit:
    guess = int(input("guess the number: "))
    guess_count +=1
    if guess == correct_number:
        print("you won")
        break
else:
    print("sorry you lost")