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
    list_phrases = []
    if not os.path.exists("20q.txt") or "--new" in sys.argv:
        print("No saved data 20q.txt file found, so creating a new database...")
        print()
        list_phrases.append(["Does it quack?", "duck", "pig"])
        with open('20q.txt', 'w') as outfile:
            json.dump(list_phrases, outfile)
    else:
        print("Using existing database 20q.txt\n")
        with open('20q.txt') as data_file:
             list_phrases = json.load(data_file)

    current = 0
    question = 0
    not_there_yet = True
    happy_to_play = True

    while not_there_yet:
            question = question + 1
            print(list_phrases[current][0], " - answer Y or N")
            ans = input().upper()
            if ans == "Y":
                    branch = 1
            else:
                    branch = 2
            if isinstance (list_phrases[current][branch], str):
                guess = str(list_phrases[current][branch])
                print("I guess, a", guess, "- am I right? (Y or N)")
                ans = input().upper()
                if ans == "Y":
                    print("Yah! I got your animal in ", question, " questions.\n\n\n")
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
                        " , but not for a ", list_phrases[current][branch])
                    question = input()
                    list_phrases.append([question, animal, guess])
                    [current][branch] = len(list_phrases)-1

                    with open('20q.txt', 'w') as outfile:
                        json.dump(list_phrases, outfile)
                else:
                        not_there_yet = False
                        print("Quitting...")
                not_there_yet = False
                question = 0
                current = 0
                print("\n\n\nThanks! Now, do you want to play again? (Y or N)")
                ans = input().upper()
                if ans == "N":
                    happy_to_play =  False
                else:
                    print("Cool! We will restart in a second...")
                    time.sleep(2)
            else:                           
                type(list_phrases[current][branch])
                current = int(list_phrases[current][branch])
print("OK, bye!")
exit()
