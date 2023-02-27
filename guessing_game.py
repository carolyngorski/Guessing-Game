import random;

n = random.randint(1,10)
print(" I am thinking of a number between 1 and 10")
running = True

while running:
    guess_str = input("Take a guess ")
    guess = int(guess_str)
    if guess == n:
      print(" Well done! You guessed the number")
      running = False
    elif guess <n:
      print("try a bigger number:")

    else:
        print("Try a smaller number:")
        
