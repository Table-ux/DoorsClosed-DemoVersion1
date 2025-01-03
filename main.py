import sys
import time
import os

def slow_print(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()
    
slow_print("Warning! This program is developed by the government of the United States of America. "
           "Do not run this code unless you are a member of the United States police law industry.\n", 0.05)

slow_print("___________________________________________________________________________________________________________________________________________________________________________\n", 0.05)

slow_print("Welcome to the official police newbie training Python program. This program was developed to train newbie 911 dispatchers.\n", 0.05)

slow_print("In today's test, you will be tested on your fight or flight response. Please be noted that the following content may be disturbing.\n", 0.05)

slow_print("Please type 'yes' to proceed or 'no' to exit.\n", 0.05)

choice = input().strip().lower()

if choice == "yes":
    slow_print("Task one.\n", 0.05)
    slow_print("In task one, you will get a call from ~*~*%<¥,£>,#^~+%.*^<€},¥%,€+^+,#*\n", 0.05)
    slow_print("Please type 'start task' to continue.\n", 0.05)
elif choice == "no":
    slow_print("So you're telling me you've gotten the code just to fuck around, you little cocksucker?\n", 0.05)
    mess = input().strip().lower()

    if mess == "yes":
        slow_print("Fuck you\n", 0.05)
        exit(0)
    else:
        slow_print("U blind or smthn? Can't u read?\n", 0.05)
        slow_print("Whatever, I'm just gonna end the program here.\n", 0.05)
        exit(0)
else:
    slow_print("Invalid input. Please restart the program and enter 'yes' or 'no'.\n", 0.05)
    exit(0)

task = input().strip().lower()

if task == "start task":
    print("*you get a phone call*")
    slow_print("Please type 'answer' to answer.\n", 0.05)
    answed = input().strip().lower()

    if answed == "answer":
        slow_print("…\n", 0.01)
        reply = input("Enter here to reply: ")
        slow_print("…\n", 0.01)
else:
    slow_print("…\n", 0.01)

slow_print("A technical error has occured while running the program. You will be directly moved to Task 2. Please type start task to start the task.\n", 0.05)

Task2 = input().strip().lower()

if Task2 == "start task":
    slow_print("Task 2.", 0.05)
    slow_print("Please note that checking whats behind you in this task, will lead to death. Do not turn away from your screen whatsoever to ensure your safety.\n", 0.05)
    slow_print("In this task, you will need to—————————————————————————————————————————————————————————————————————————— kill Huston.\n", 0.05)
else:
    slow_print("Invalid input. Please restart the program and enter 'start task'.\n", 0.05)


os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(10)

slow_print("-Julian…\n", 0.5)
slow_print("-I know you're there Julian…\n", 0.5)
slow_print("-It hurts… to know that you're avoiding me…\n", 0.5)
slow_print("-Please forgive me… Julian…\n", 0.5)
slow_print("-That's the only thing I'm asking you…\n", 0.5)
slow_print("-…\n", 0.005)
slow_print("-I'm running out of time dear…\n", 0.5)
slow_print("-Please… don't die out there this time…\n", 0.5)
slow_print("-Daddy is going to miss you… see you… Julian…\n", 1)


time.sleep(5)
os.system('cls' if os.name == 'nt' else 'clear')

slow_print("End of demo version 1, hope yall enjoyed.\n", 0.05)
slow_print("Currently developing demo version 2. If anyone got some ideas, text me on discord.\n", 0.05)
slow_print("THANK YOU A LOT for playing <3. Took me about 4 days to write the code, it could've been longer without ChatGPT ;)\n", 0.05)

slow_print("Credits:\n", 0.05)
slow_print("Table\n", 0.05)
slow_print("ChatGPT\n", 0.05)

slow_print("SPECIAL THANKS\n", 0.05)
slow_print("ChatGPT\n", 0.05)
slow_print("Youtube Tutorials\n", 0.05)
slow_print("My patience and attention span\n", 0.05)
slow_print("My iPad for crashing only 5 times while testing the code (especially at the end for some reason)\n", 0.05)

exit(0)
