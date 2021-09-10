#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import random


user_action = input("Ready to play? ")
computerscore = 0
userscore = 0
tiescore = 0
totalscore = (computerscore + userscore + tiescore)
userchoicep = 0
userchoicer = 0
userchoices = 0



while user_action != 'quit':
#computer chooses rock, paper, scissors

    def biasedchoice():
        rchoice = userchoicer
        pchoice = userchoicep
        schoice = userchoices
        if rchoice > (pchoice + schoice):
            bias_choice = 'paper'

        if pchoice > (rchoice + schoice):
            bias_choice = 'scissors'

        if schoice > (rchoice + pchoice):
            bias_choice = 'rock'
        else:
            bias_choice = random.choice(possible_actions)

        return bias_choice

#computer asks for human input :chooses rock, paper, scissors
    user_action = input("Enter a choice: ('rock', 'paper', 'scissors', 'quit'): ")
    possible_actions = ['rock', 'paper', 'scissors']
    computer_action = biasedchoice()
    if user_action == computer_action:
        tiescore=tiescore+1
        print("Both players selected", {user_action} ,"It's a draw!")
    if user_action == 'rock':
        userchoicer = userchoicer + 1
        if computer_action == 'scissors':
            print("User wins! Rock smashes scissors! so Rock beats Scissors")
            userscore=userscore+1
        elif computer_action == 'paper':
            print("Computer wins! Paper covers rock so Paper beats Rock")
            computerscore=computerscore+1
    elif user_action == 'paper':
        userchoicep = userchoicep + 1
        if computer_action == 'rock':
            print("User wins!Paper covers rock, so Paper beats Rock")
            userscore=userscore+1
        elif computer_action == 'scissors':
            print("Computer wins! Scissors can cut up paper, so Scissors beat Paper")
            computerscore=computerscore+1
    elif user_action == 'scissors':
        userchoices = userchoices + 1
        if computer_action == 'paper':
            print("User wins! Scissors can cut up paper, so Scissors beat Paper")
            userscore=userscore+1
        elif computer_action == 'rock':
            print("Computer wins! Rock smashes scissors! so Rock beats Scissors")
            computerscore=computerscore+1
    elif user_action == 'quit':
        print("Number of games played = ",{(userscore+computerscore+tiescore)}," games")
        print("Number of times user won = ",{userscore}," games")
        break


# In[ ]:





# In[ ]:




