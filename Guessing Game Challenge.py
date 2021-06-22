'''
The Challenge:

Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:

1- If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
2- On a player's first turn, if their guess is 
  within 10 of the number, return "WARM!"
  further than 10 away from the number, return "COLD!"
3- On all subsequent turns, if a guess is
  closer to the number than the previous guess return "WARMER!"
  farther from the number than the previous guess, return "COLDER!"
4- When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!
'''

import random

print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

x = random.randint(1,100)
keep_try = True
guesses = [0]
while keep_try:
    guess_no = int(input("Your Guess: "))
    
    if guess_no<1 or guess_no>100:
        print("OUT OF BOUND! Please try again:")
        continue
    if guess_no == x:
        print("Correct Guess")
        break
    
    guesses.append(guess_no)
    
    if guesses[-2]:
        if abs(x-guesses[-2])>abs(x-guess_no):
            print("Warmer!")
        else:
            print("Colder!")
    else:
        if abs(x-guess_no)<=10:
            print("Warm!")
        else:
            print("Cold!")
            
print(f"Total Guesses are = {len(guesses)}")
