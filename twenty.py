#!/usr/bin/env python
import json
import os
import sys
import time

def clear() -> None:
    """clearing the console"""
    os.system('cls' if os.name == 'nt' else 'clear')

happy_to_play = True
while happy_to_play:
    clear()
    print("\n\n\n\n")
    print("This is a little game. I will guess the creature that")
    print("you are thinking of in 20 questions or less!")
    print(" ")
    q = []
    if not os.path.exists("20q.txt") or "--new" in sys.argv:
        print("No saved data 20q.txt file found, so creating a new database...")
        print()
        q.append(["Does it quack?", "duck", "pig"])
        with open('20q.txt', 'w') as outfile:
            json.dump(q, outfile)
    else:
        print("Using existing database 20q.txt\n")
        with open('20q.txt') as data_file:
             q = json.load(data_file)

    curr = 0
    questions = 0
    not_there_yet = True
    happy_to_play = True

    while not_there_yet:
            questions = questions + 1
            print(q[curr][0], " - answer Y or N")
            ans = input().upper()
            if ans == "Y":
                    branch = 1
            else:
                    branch = 2
            if isinstance (q[curr][branch], str):
                guess = str(q[curr][branch])
                print("I guess, a", guess, "- am I right? (Y or N)")
                ans = input().upper()
                if ans == "Y":
                    print("Yah! I got your animal in ", questions, " questions.\n\n\n")
                    not_there_yet = False
                elif ans == "N":
                    print("What is it?")
                    animal = input()
                    print(animal)
                    animal_head = animal.split()[0].lower()
                    if (animal_head == "a") or (animal_head == "an"):
                        animal = ' '.join(animal.split()[1:])
                    else:
                        animal = animal

                    print("Thanks! Now, give me a new question that will be true for a", animal, \
                        " , but not for a ", q[curr][branch])
                    question = input()
                    q.append([question, animal, guess])
                    [curr][branch] = len(q)-1

                    with open('20q.txt', 'w') as outfile:
                        json.dump(q, outfile)
                else:
                        not_there_yet = False
                        print("Quitting...")
                not_there_yet = False
                questions = 0
                curr = 0
                print("\n\n\nThanks! Now, do you want to play again? (Y or N)")
                ans = input().upper()
                if ans == "N":
                    happy_to_play =  False
                else:
                    print("Cool! We will restart in a second...")
                    time.sleep(2)
            else:                           
                type(q[curr][branch])
                curr = int(q[curr][branch])
print("OK, bye!")
exit()
