from Topics import *
import os #clear screen
import itertools #making loading spinner effect
import time #for the loading time
import sys #print text without adding new line
from colorama import Fore, Style, init #to put color on text
init()

os.system('cls') #os.system('cls'): Use to clear Screen


#Loading Animation
spinner = itertools.cycle(['|', '/', '-', '\\'])

for _ in range(20):
    sys.stdout.write('\rLoading ' + next(spinner))
    sys.stdout.flush()
    time.sleep(0.1)

print(Fore.GREEN + '\rDone!     ') #add color on text
print(Style.RESET_ALL) #reset color

print("\n") #new line
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("|" + Fore.BLUE + "\tWelcome to my Finals Project at ITCS-102\t" + Style.RESET_ALL + "|")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("\n")
name = input(" Username (*)\nPlease input your name here --->   ")
os.system('cls')

spinner = itertools.cycle(['|', '/', '-', '\\'])

for _ in range(20):
    sys.stdout.write('\rLoading ' + next(spinner))
    sys.stdout.flush()
    time.sleep(0.1)

print(Fore.GREEN + '\rDone!     ')
print(Style.RESET_ALL)

print(Fore.YELLOW + "\t\t\tIMPORTANT NOTICE")
print("\n")
print(Fore.YELLOW + " • To add color for the text Please run the command ( pip install colorama ) \n   first and wait until you see \"Successfully installed colorama\" for better\n   experience and understanding. If ( pip ) doesn't work, try to \n   run ( python -m pip colorama ). ")
print(" • For Activity 28, the command ( pip3 install pygame ) is required to run first\n   to activate the game. Otherwise, it will crash.")
print(Style.RESET_ALL)

print("\n")
isContinue = input("Press ENTER to continue:  ").lower()
os.system('cls')
spinner = itertools.cycle(['|', '/', '-', '\\'])

for _ in range(20):
    sys.stdout.write('\rLoading ' + next(spinner))
    sys.stdout.flush()
    time.sleep(0.1)

print(Fore.GREEN + '\rDone!     ')
print(Style.RESET_ALL)



print("\n")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(f"|Welcome {name}, to Interactive Menu Program.\t\t|") #f string
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("\n")
print("|=======================================================|")
print("|By: Ken Josua Pasamba\t\t\t\t\t|\n|BSIT Student\t\t\t\t\t\t|\n|Section 1A\t\t\t\t\t\t|")
print("|=======================================================|")
print("\n")
#Main menu
while True:
    print("|-------------------------------------------------------|")
    print("|Choose One Options From Below:\t\t\t\t|")
    print("|-------------------------------------------------------|")
    print("|A - Activities\t\t\t\t\t\t|\n|B - Code_challenges\t\t\t\t\t|\n|Q - Quit\t\t\t\t\t\t|")
    print("|-------------------------------------------------------|")
    print("\n")
    choice = input(Fore.YELLOW + " Enter your answer here:" + Style.RESET_ALL).lower()
    
    #Submenu
    if choice == "a":
        os.system('cls')
        while True:

            spinner = itertools.cycle(['|', '/', '-', '\\'])

            for _ in range(20):
                sys.stdout.write('\rLoading ' + next(spinner))
                sys.stdout.flush()
                time.sleep(0.1)

            print(Fore.GREEN + '\rDone!     ') 
            print(Style.RESET_ALL)          

            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("|" + Fore.BLUE + "\t\t\tActivities\t\t\t" + Style.RESET_ALL + "|")
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("\n")
            print("|-------------------------------------------------------|")
            print("|\t\t\tPage 1/3\t\t\t|")
            print("|-------------------------------------------------------|")
            print("| A - Activity1  -  Hello World\t\t\t\t|\n| B - Activity2  -  Name Input\t\t\t\t|\n| C - Activity3  -  Formatting\t\t\t\t|\n| D - Activity4  -  String Length\t\t\t|\n| E - Activity5  -  Data Type\t\t\t\t|\n| F - Activity6  -  Arithmetic\t\t\t\t|\n| G - Activity7  -  Values\t\t\t\t|\n| H - Activity8  -  Comparison\t\t\t\t|\n| I - Activity9  -  Logic\t\t\t\t|\n| J - Activity10 -  Student Fare\t\t\t|")
            print("|-------------------------------------------------------|")
            print("| N - Next\t\t\t\t\t\t|\n| Q - Quit\t\t\t\t\t\t|")
            print("|-------------------------------------------------------|")
            print("\n")
            choose = input(Fore.YELLOW + "what program/topic would you like to run ->" + Style.RESET_ALL).lower()

            if choose == 'a':
                os.system('cls')
                spinner = itertools.cycle(['|', '/', '-', '\\'])

                for _ in range(20):
                    sys.stdout.write('\rLoading ' + next(spinner))
                    sys.stdout.flush()
                    time.sleep(0.1)

                print(Fore.GREEN + '\rDone!     ')
                print(Style.RESET_ALL)                
                activity1()
                continue
            elif choose == 'b':
                os.system('cls')
                spinner = itertools.cycle(['|', '/', '-', '\\'])

                for _ in range(20):
                    sys.stdout.write('\rLoading ' + next(spinner))
                    sys.stdout.flush()
                    time.sleep(0.1)

                print(Fore.GREEN + '\rDone!     ')
                print(Style.RESET_ALL)                          
                activity2()
                continue
            elif choose == 'c':
                os.system('cls')
                spinner = itertools.cycle(['|', '/', '-', '\\'])

                for _ in range(20):
                    sys.stdout.write('\rLoading ' + next(spinner))
                    sys.stdout.flush()
                    time.sleep(0.1)

                print(Fore.GREEN + '\rDone!     ')
                print(Style.RESET_ALL)                          
                activity3()
                continue
            elif choose == 'd':
                os.system('cls')
                spinner = itertools.cycle(['|', '/', '-', '\\'])

                for _ in range(20):
                    sys.stdout.write('\rLoading ' + next(spinner))
                    sys.stdout.flush()
                    time.sleep(0.1)

                print(Fore.GREEN + '\rDone!     ')
                print(Style.RESET_ALL)          
                activity4()
                continue
            elif choose == 'e':
                os.system('cls')
                spinner = itertools.cycle(['|', '/', '-', '\\'])

                for _ in range(20):
                    sys.stdout.write('\rLoading ' + next(spinner))
                    sys.stdout.flush()
                    time.sleep(0.1)

                print(Fore.GREEN + '\rDone!     ')
                print(Style.RESET_ALL)          
                activity5()
                continue
            elif choose == 'f':
                os.system('cls')
                spinner = itertools.cycle(['|', '/', '-', '\\'])

                for _ in range(20):
                    sys.stdout.write('\rLoading ' + next(spinner))
                    sys.stdout.flush()
                    time.sleep(0.1)

                print(Fore.GREEN + '\rDone!     ')
                print(Style.RESET_ALL)          
                activity6()
                continue
            elif choose == 'g':
                os.system('cls')
                spinner = itertools.cycle(['|', '/', '-', '\\'])

                for _ in range(20):
                    sys.stdout.write('\rLoading ' + next(spinner))
                    sys.stdout.flush()
                    time.sleep(0.1)

                print(Fore.GREEN + '\rDone!     ')
                print(Style.RESET_ALL)          
                activity7()
                continue
            elif choose == 'h':
                os.system('cls')
                spinner = itertools.cycle(['|', '/', '-', '\\'])

                for _ in range(20):
                    sys.stdout.write('\rLoading ' + next(spinner))
                    sys.stdout.flush()
                    time.sleep(0.1)

                print(Fore.GREEN + '\rDone!     ')
                print(Style.RESET_ALL)          
                activity8()
                continue
            elif choose == 'i':
                os.system('cls')
                spinner = itertools.cycle(['|', '/', '-', '\\'])

                for _ in range(20):
                    sys.stdout.write('\rLoading ' + next(spinner))
                    sys.stdout.flush()
                    time.sleep(0.1)

                print(Fore.GREEN + '\rDone!     ')
                print(Style.RESET_ALL)          
                activity9()
                continue
            elif choose == 'j':
                os.system('cls')
                spinner = itertools.cycle(['|', '/', '-', '\\'])

                for _ in range(20):
                    sys.stdout.write('\rLoading ' + next(spinner))
                    sys.stdout.flush()
                    time.sleep(0.1)

                print(Fore.GREEN + '\rDone!     ')
                print(Style.RESET_ALL)          
                activity10()
                continue
            elif choose == 'n':
                os.system('cls')
                while True:

                    spinner = itertools.cycle(['|', '/', '-', '\\'])

                    for _ in range(20):
                        sys.stdout.write('\rLoading ' + next(spinner))
                        sys.stdout.flush()
                        time.sleep(0.1)

                    print(Fore.GREEN + '\rDone!     ')
                    print(Style.RESET_ALL)

                    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                    print("|" + Fore.BLUE + "\t\t\tActivities\t\t\t" + Style.RESET_ALL + "|")
                    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                    print("\n")
                    print("|-------------------------------------------------------|")
                    print("|\t\t\tPage 2/3\t\t\t|")
                    print("|-------------------------------------------------------|")
                    print("| A - Activity11  -  Thermometer\t\t\t|\n| B - Activity12  -  Loop\t\t\t\t|\n| C - Activity13  -  Loop Number\t\t\t|\n| D - Activity14  -  For Loop\t\t\t\t|\n| E - Activity15  -  Loop Sum\t\t\t\t|\n| F - Activity16  -  Vertical Loop\t\t\t|\n| G - Activity17  -  Grid Loop\t\t\t\t|\n| H - Activity18  -  Triangular Loop\t\t\t|\n| I - Activity19  -  Triangular Loop (Symbols)\t\t|\n| J - Activity20  -  Grid Loop (Symbols)\t\t|")
                    print("|-------------------------------------------------------|")
                    print("| N - Next\t\t\t\t\t\t|\n| Q - Quit\t\t\t\t\t\t|")     
                    print("|-------------------------------------------------------|")
                    print("\n")               
                    choose = input(Fore.YELLOW + "what program/topic would you like to run ->" + Style.RESET_ALL).lower()

                    if choose == 'a':
                        os.system('cls')
                        spinner = itertools.cycle(['|', '/', '-', '\\'])

                        for _ in range(20):
                            sys.stdout.write('\rLoading ' + next(spinner))
                            sys.stdout.flush()
                            time.sleep(0.1)

                        print(Fore.GREEN + '\rDone!     ')
                        print(Style.RESET_ALL)          
                        activity11()
                        continue
                    elif choose == 'b':
                        os.system('cls')
                        spinner = itertools.cycle(['|', '/', '-', '\\'])

                        for _ in range(20):
                            sys.stdout.write('\rLoading ' + next(spinner))
                            sys.stdout.flush()
                            time.sleep(0.1)

                        print(Fore.GREEN + '\rDone!     ')
                        print(Style.RESET_ALL)     
                        activity12()
                        continue
                    elif choose == 'c':
                        os.system('cls')
                        spinner = itertools.cycle(['|', '/', '-', '\\'])

                        for _ in range(20):
                            sys.stdout.write('\rLoading ' + next(spinner))
                            sys.stdout.flush()
                            time.sleep(0.1)

                        print(Fore.GREEN + '\rDone!     ')
                        print(Style.RESET_ALL)     
                        activity13()
                        continue
                    elif choose == 'd':
                        os.system('cls')
                        spinner = itertools.cycle(['|', '/', '-', '\\'])

                        for _ in range(20):
                            sys.stdout.write('\rLoading ' + next(spinner))
                            sys.stdout.flush()
                            time.sleep(0.1)

                        print(Fore.GREEN + '\rDone!     ')
                        print(Style.RESET_ALL)     
                        activity14()
                        continue
                    elif choose == 'e':
                        os.system('cls')
                        spinner = itertools.cycle(['|', '/', '-', '\\'])

                        for _ in range(20):
                            sys.stdout.write('\rLoading ' + next(spinner))
                            sys.stdout.flush()
                            time.sleep(0.1)

                        print(Fore.GREEN + '\rDone!     ')
                        print(Style.RESET_ALL)     
                        activity15()
                        continue
                    elif choose == 'f':
                        os.system('cls')
                        spinner = itertools.cycle(['|', '/', '-', '\\'])

                        for _ in range(20):
                            sys.stdout.write('\rLoading ' + next(spinner))
                            sys.stdout.flush()
                            time.sleep(0.1)

                        print(Fore.GREEN + '\rDone!     ')
                        print(Style.RESET_ALL)     
                        activity16()
                        continue
                    elif choose == 'g':
                        os.system('cls')
                        spinner = itertools.cycle(['|', '/', '-', '\\'])

                        for _ in range(20):
                            sys.stdout.write('\rLoading ' + next(spinner))
                            sys.stdout.flush()
                            time.sleep(0.1)

                        print(Fore.GREEN + '\rDone!     ')
                        print(Style.RESET_ALL)     
                        activity17()
                        continue
                    elif choose == 'h':
                        os.system('cls')
                        spinner = itertools.cycle(['|', '/', '-', '\\'])

                        for _ in range(20):
                            sys.stdout.write('\rLoading ' + next(spinner))
                            sys.stdout.flush()
                            time.sleep(0.1)

                        print(Fore.GREEN + '\rDone!     ')
                        print(Style.RESET_ALL)     
                        activity18()
                        continue
                    elif choose == 'i':
                        os.system('cls')
                        spinner = itertools.cycle(['|', '/', '-', '\\'])

                        for _ in range(20):
                            sys.stdout.write('\rLoading ' + next(spinner))
                            sys.stdout.flush()
                            time.sleep(0.1)

                        print(Fore.GREEN + '\rDone!     ')
                        print(Style.RESET_ALL)     
                        activity19()
                        continue
                    elif choose == 'j':
                        os.system('cls')
                        spinner = itertools.cycle(['|', '/', '-', '\\'])

                        for _ in range(20):
                            sys.stdout.write('\rLoading ' + next(spinner))
                            sys.stdout.flush()
                            time.sleep(0.1)

                        print(Fore.GREEN + '\rDone!     ')
                        print(Style.RESET_ALL)     
                        activity20()
                        continue
                    elif choose == 'n':
                        os.system('cls')
                        while True:

                            spinner = itertools.cycle(['|', '/', '-', '\\'])

                            for _ in range(20):
                                sys.stdout.write('\rLoading ' + next(spinner))
                                sys.stdout.flush()
                                time.sleep(0.1)

                            print(Fore.GREEN + '\rDone!     ')
                            print(Style.RESET_ALL)

                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("|" + Fore.BLUE + "\t\t\tActivities\t\t\t" + Style.RESET_ALL + "|")
                            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                            print("\n")
                            print("|-------------------------------------------------------|")
                            print("|\t\t\tPage 3/3\t\t\t|")
                            print("|-------------------------------------------------------|")
                            print("| A - Activity21  -  Washing Machine\t\t\t|\n| B - Activity22  -  Guess Number\t\t\t|\n| C - Activity23  -  List & Function\t\t\t|\n| D - Activity24  -  Creating Functions\t\t\t|\n| E - Activity25  -  Compiler\t\t\t\t|\n| F - Activity26  -  Dictionary\t\t\t\t|\n| G - Activity27  -  Adding Dictionary\t\t\t|\n| H - Activity28  -  Snake Game\t\t\t\t|")
                            print("|-------------------------------------------------------|")
                            print("| Q - Quit\t\t\t\t\t\t|")   
                            print("|-------------------------------------------------------|")
                            print("\n")
                            choose = input(Fore.YELLOW + "what program/topic would you like to run ->" + Style.RESET_ALL).lower()
                            if choose == 'a':
                                os.system('cls')
                                spinner = itertools.cycle(['|', '/', '-', '\\'])

                                for _ in range(20):
                                    sys.stdout.write('\rLoading ' + next(spinner))
                                    sys.stdout.flush()
                                    time.sleep(0.1)

                                print(Fore.GREEN + '\rDone!     ')
                                print(Style.RESET_ALL)     
                                activity21()
                                continue
                            elif choose == 'b':
                                os.system('cls')
                                spinner = itertools.cycle(['|', '/', '-', '\\'])

                                for _ in range(20):
                                    sys.stdout.write('\rLoading ' + next(spinner))
                                    sys.stdout.flush()
                                    time.sleep(0.1)

                                print(Fore.GREEN + '\rDone!     ')
                                print(Style.RESET_ALL)     
                                activity22()
                                continue
                            elif choose == 'c':
                                os.system('cls')
                                spinner = itertools.cycle(['|', '/', '-', '\\'])

                                for _ in range(20):
                                    sys.stdout.write('\rLoading ' + next(spinner))
                                    sys.stdout.flush()
                                    time.sleep(0.1)

                                print(Fore.GREEN + '\rDone!     ')
                                print(Style.RESET_ALL)     
                                activity23()
                                continue
                            elif choose == 'd':
                                os.system('cls')
                                spinner = itertools.cycle(['|', '/', '-', '\\'])

                                for _ in range(20):
                                    sys.stdout.write('\rLoading ' + next(spinner))
                                    sys.stdout.flush()
                                    time.sleep(0.1)

                                print(Fore.GREEN + '\rDone!     ')
                                print(Style.RESET_ALL)     
                                activity24()
                                continue
                            elif choose == 'e':
                                os.system('cls')
                                spinner = itertools.cycle(['|', '/', '-', '\\'])

                                for _ in range(20):
                                    sys.stdout.write('\rLoading ' + next(spinner))
                                    sys.stdout.flush()
                                    time.sleep(0.1)

                                print(Fore.GREEN + '\rDone!     ')
                                print(Style.RESET_ALL)     
                                activity25()
                                continue
                            elif choose == 'f':
                                os.system('cls')
                                spinner = itertools.cycle(['|', '/', '-', '\\'])

                                for _ in range(20):
                                    sys.stdout.write('\rLoading ' + next(spinner))
                                    sys.stdout.flush()
                                    time.sleep(0.1)

                                print(Fore.GREEN + '\rDone!     ')
                                print(Style.RESET_ALL)     
                                activity26()
                                continue
                            elif choose == 'g':
                                os.system('cls')
                                spinner = itertools.cycle(['|', '/', '-', '\\'])

                                for _ in range(20):
                                    sys.stdout.write('\rLoading ' + next(spinner))
                                    sys.stdout.flush()
                                    time.sleep(0.1)

                                print(Fore.GREEN + '\rDone!     ')
                                print(Style.RESET_ALL)     
                                activity27()
                                continue
                            elif choose == 'h':
                                os.system('cls')
                                spinner = itertools.cycle(['|', '/', '-', '\\'])

                                for _ in range(20):
                                    sys.stdout.write('\rLoading ' + next(spinner))
                                    sys.stdout.flush()
                                    time.sleep(0.1)

                                print(Fore.GREEN + '\rDone!     ')
                                print(Style.RESET_ALL)     
                                activity28()
                                continue
                            elif choose == 'q':
                                os.system('cls')
                                print("\t\t\t\t\t\tSystem Exit!")
                                break
                            else:
                                os.system('cls')
                                print(Fore.RED + "\t\t\t\t\t\tInvalid Input, Please try again!")
                                print(Style.RESET_ALL)

                    elif choose == 'q':
                        os.system('cls')
                        print("\t\t\t\t\t\tSystem Exit!")
                        break
                    else:
                        os.system('cls')
                        print(Fore.RED + "\t\t\t\t\t\tInvalid Input, Please try again!")
                        print(Style.RESET_ALL)
            elif choose == 'q':
                os.system('cls')
                print("\t\t\t\t\t\tSystem Exit!")
                break
            else:
                os.system('cls')
                print(Fore.RED + "\t\t\t\t\t\tInvalid Input, Please try again!")
                print(Style.RESET_ALL)
    elif choice == "b":
        os.system('cls')
        while True:

            spinner = itertools.cycle(['|', '/', '-', '\\'])

            for _ in range(20):
                sys.stdout.write('\rLoading ' + next(spinner))
                sys.stdout.flush()
                time.sleep(0.1)

            print(Fore.GREEN + '\rDone!     ')
            print(Style.RESET_ALL)


            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("|" + Fore.BLUE + "\t\t\tCode_Challenges\t\t\t" + Style.RESET_ALL + "|")
            print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
            print("\n")
            print("|-------------------------------------------------------|")
            print("|\t\t\tPage 1/2\t\t\t|")
            print("|-------------------------------------------------------|")
            print("| A - Code_challenge1  -  Name Input (\\t,\\n)\t\t|\n| B - Code_challenge2  -  Deposite Calculator\t\t|\n| C - Code_challenge3  -  Login Credentials\t\t|\n| D - Code_challenge4  -  Odd/Even Checker\t\t|\n| E - Code_challenge5  -  Manga Recomender\t\t|\n| F - Code_challenge6  -  Factorial\t\t\t|\n| G - Code_challenge7  -  Odd Sum\t\t\t|\n| H - Code_challenge8  -  Multiplication Table\t\t|\n| I - Code_challenge9  -  Countdown Sim\t\t\t|\n| J - Code_challenge10 -  Triangle Loop\t\t\t|")
            print("|-------------------------------------------------------|")
            print("| N - Next\t\t\t\t\t\t|\n| Q - Quit\t\t\t\t\t\t|")
            print("|-------------------------------------------------------|")
            print("\n")
            choose = input(Fore.YELLOW + "what program/topic would you like to run ->" + Style.RESET_ALL).lower()
            if choose == 'a':
                os.system('cls')
                spinner = itertools.cycle(['|', '/', '-', '\\'])

                for _ in range(20):
                    sys.stdout.write('\rLoading ' + next(spinner))
                    sys.stdout.flush()
                    time.sleep(0.1)

                print(Fore.GREEN + '\rDone!     ')
                print(Style.RESET_ALL)     
                code_challenge1()
                continue
            elif choose == 'b':
                os.system('cls')
                spinner = itertools.cycle(['|', '/', '-', '\\'])

                for _ in range(20):
                    sys.stdout.write('\rLoading ' + next(spinner))
                    sys.stdout.flush()
                    time.sleep(0.1)

                print(Fore.GREEN + '\rDone!     ')
                print(Style.RESET_ALL)     
                code_challenge2()
                continue
            elif choose == 'c':
                os.system('cls')
                spinner = itertools.cycle(['|', '/', '-', '\\'])

                for _ in range(20):
                    sys.stdout.write('\rLoading ' + next(spinner))
                    sys.stdout.flush()
                    time.sleep(0.1)

                print(Fore.GREEN + '\rDone!     ')
                print(Style.RESET_ALL)     
                code_challenge3()
                continue
            elif choose == 'd':
                os.system('cls')
                spinner = itertools.cycle(['|', '/', '-', '\\'])

                for _ in range(20):
                    sys.stdout.write('\rLoading ' + next(spinner))
                    sys.stdout.flush()
                    time.sleep(0.1)

                print(Fore.GREEN + '\rDone!     ')
                print(Style.RESET_ALL)     
                code_challenge4()
                continue
            elif choose == 'e':
                os.system('cls')
                spinner = itertools.cycle(['|', '/', '-', '\\'])

                for _ in range(20):
                    sys.stdout.write('\rLoading ' + next(spinner))
                    sys.stdout.flush()
                    time.sleep(0.1)

                print(Fore.GREEN + '\rDone!     ')
                print(Style.RESET_ALL)     
                code_challenge5()
                continue
            elif choose == 'f':
                os.system('cls')
                spinner = itertools.cycle(['|', '/', '-', '\\'])

                for _ in range(20):
                    sys.stdout.write('\rLoading ' + next(spinner))
                    sys.stdout.flush()
                    time.sleep(0.1)

                print(Fore.GREEN + '\rDone!     ')
                print(Style.RESET_ALL)     
                code_challenge6()
                continue
            elif choose == 'g':
                os.system('cls')
                spinner = itertools.cycle(['|', '/', '-', '\\'])

                for _ in range(20):
                    sys.stdout.write('\rLoading ' + next(spinner))
                    sys.stdout.flush()
                    time.sleep(0.1)

                print(Fore.GREEN + '\rDone!     ')
                print(Style.RESET_ALL)     
                code_challenge7()
                continue
            elif choose == 'h':
                os.system('cls')
                spinner = itertools.cycle(['|', '/', '-', '\\'])

                for _ in range(20):
                    sys.stdout.write('\rLoading ' + next(spinner))
                    sys.stdout.flush()
                    time.sleep(0.1)

                print(Fore.GREEN + '\rDone!     ')
                print(Style.RESET_ALL)     
                code_challenge8()
                continue
            elif choose == 'i':
                os.system('cls')
                spinner = itertools.cycle(['|', '/', '-', '\\'])

                for _ in range(20):
                    sys.stdout.write('\rLoading ' + next(spinner))
                    sys.stdout.flush()
                    time.sleep(0.1)

                print(Fore.GREEN + '\rDone!     ')
                print(Style.RESET_ALL)     
                code_challenge9()
                continue
            elif choose == 'j':
                os.system('cls')
                spinner = itertools.cycle(['|', '/', '-', '\\'])

                for _ in range(20):
                    sys.stdout.write('\rLoading ' + next(spinner))
                    sys.stdout.flush()
                    time.sleep(0.1)

                print(Fore.GREEN + '\rDone!     ')
                print(Style.RESET_ALL)     
                code_challenge10()
                continue
            elif choose == 'n':
                os.system('cls')
                while True:

                    spinner = itertools.cycle(['|', '/', '-', '\\'])

                    for _ in range(20):
                        sys.stdout.write('\rLoading ' + next(spinner))
                        sys.stdout.flush()
                        time.sleep(0.1)

                    print(Fore.GREEN + '\rDone!     ')
                    print(Style.RESET_ALL)

                    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                    print("|" + Fore.BLUE + "\t\t\tCode_Challenges\t\t\t" + Style.RESET_ALL + "|")
                    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                    print("\n")
                    print("|-------------------------------------------------------|")
                    print("|\t\t\tPage 2/2\t\t\t|")
                    print("|-------------------------------------------------------|")
                    print("| A - Code_challenge11  -  Diamond Loop\t\t\t|\n| B - Code_challenge12  -  Triangle Loop (NUmbers)\t|\n| C - Code_challenge13  -  Arrow Loop\t\t\t|\n| D - Code_challenge14  -  Odd Number Compiler\t\t|\n| E - Code_challenge15  -  Anime Lister\t\t\t|\n| F - Code_challenge16  -  Student Information Recorder\t|")
                    print("|-------------------------------------------------------|")
                    print("| Q - Quit\t\t\t\t\t\t|")   
                    print("|-------------------------------------------------------|")
                    print("\n")
                    choose = input(Fore.YELLOW + "what program/topic would you like to run ->" + Style.RESET_ALL).lower()


                    if choose == 'a':
                        os.system('cls')
                        spinner = itertools.cycle(['|', '/', '-', '\\'])

                        for _ in range(20):
                            sys.stdout.write('\rLoading ' + next(spinner))
                            sys.stdout.flush()
                            time.sleep(0.1)

                        print(Fore.GREEN + '\rDone!     ')
                        print(Style.RESET_ALL)     
                        code_challenge11()
                        continue
                    elif choose == 'b':
                        os.system('cls')
                        spinner = itertools.cycle(['|', '/', '-', '\\'])

                        for _ in range(20):
                            sys.stdout.write('\rLoading ' + next(spinner))
                            sys.stdout.flush()
                            time.sleep(0.1)

                        print(Fore.GREEN + '\rDone!     ')
                        print(Style.RESET_ALL)     
                        code_challenge12()
                        continue
                    elif choose == 'c':
                        os.system('cls')
                        spinner = itertools.cycle(['|', '/', '-', '\\'])

                        for _ in range(20):
                            sys.stdout.write('\rLoading ' + next(spinner))
                            sys.stdout.flush()
                            time.sleep(0.1)

                        print(Fore.GREEN + '\rDone!     ')
                        print(Style.RESET_ALL)     
                        code_challenge13()
                        continue
                    elif choose == 'd':
                        os.system('cls')
                        spinner = itertools.cycle(['|', '/', '-', '\\'])

                        for _ in range(20):
                            sys.stdout.write('\rLoading ' + next(spinner))
                            sys.stdout.flush()
                            time.sleep(0.1)

                        print(Fore.GREEN + '\rDone!     ')
                        print(Style.RESET_ALL)     
                        code_challenge14()
                        continue
                    elif choose == 'e':
                        os.system('cls')
                        spinner = itertools.cycle(['|', '/', '-', '\\'])

                        for _ in range(20):
                            sys.stdout.write('\rLoading ' + next(spinner))
                            sys.stdout.flush()
                            time.sleep(0.1)

                        print(Fore.GREEN + '\rDone!     ')
                        print(Style.RESET_ALL)     
                        code_challenge15()
                        continue
                    elif choose == 'f':
                        os.system('cls')
                        spinner = itertools.cycle(['|', '/', '-', '\\'])

                        for _ in range(20):
                            sys.stdout.write('\rLoading ' + next(spinner))
                            sys.stdout.flush()
                            time.sleep(0.1)

                        print(Fore.GREEN + '\rDone!     ')
                        print(Style.RESET_ALL)     
                        code_challenge16()
                        continue
                    elif choose == 'q':
                        os.system('cls')
                        print("\t\t\t\t\t\tSystem Exit!")
                        break
                    else:
                        os.system('cls')
                        print(Fore.RED + "\t\t\t\t\t\tInvalid Input, Please try again!")
                        print(Style.RESET_ALL)
            elif choose == 'q':
                os.system('cls')
                print("\t\t\t\t\t\tSystem Exit!")
                break
            else:
                os.system('cls')
                print(Fore.RED + "\t\t\t\t\t\tInvalid Input, Please try again!")
                print(Style.RESET_ALL)
    elif choice == 'q':
        os.system('cls')
        print(Fore.GREEN + "\t\t\t\t\t\tSystem Exit!")
        print(Style.RESET_ALL)
        break
    else:
        os.system('cls')
        print(Fore.RED + "\t\t\t\t\t\tInvalid Input, Please try again!")
        print(Style.RESET_ALL)

