# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 18:27:00 2024

@author: Samruddhi
"""

import random
secret_number = random.randint(1,100)
attempts=0

print("Welcome to guess the number game!")
print("I'm thinking of a number between 1 and 100")

while True:
    try:
        guess= int(input("Your guess:"))
        attempts += 1
        
        if guess< secret_number:
            print("Try a higher number.")
        elif guess> secret_number: 
            print("Try a lower number.")
        else:
            print(f"Congratulations! you've guessed the number in {attempts} attempts.")
            break 
   
    except ValueError:
            print("Invalid input. Please enter a valid number 1 and 100. ")
            
print("Thank You for playing")