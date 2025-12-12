from topics import *
import os

name = input("Username (*)\nPlease input your name here --->   ")

print(f"welcome {name}, to Interactive Menu Program")


while True:
    print("Choose one type of Programming Exercises:")
    print("A - Activities\nB - Code_challenges\nE - Exit")
    choice = input("Enter 1 to go to submenu, or q to quit: ").lower()

    if choice == "a":
        pass
        continue

    elif choice == "1":
        print("System Exit!")
        break
    else:
        print("Invalid input, please try again:")
        continue

        while True:
            print("Submenu")
            sub = input("Enter b to go back: ")

            if choose == '1':
                os.system('cls')
                activity1()
                continue
            elif choose == '2':
                activity2()
                continue
            elif choose == '3':
                activity3()
                continue
            elif choose == '4':
                activity4()
                continue
            elif choose == '5':
                activity5()
                continue
            elif choose == '6':
                activity6()
                continue
            elif choose == '7':
                activity7()
                continue
            elif choose == '8':
                activity8()
                continue
            elif choose == '9':
                activity9()
                continue
            elif choose == '10':
                activity10()
                continue
            elif choose == '11':
                activity11()
                continue
            elif choose == '12':
                activity12()
                continue
            elif choose == '13':
                activity13()
                continue
            elif choose == '14':
                activity14()
                continue
            elif choose == '15':
                activity15()
                continue
            elif choose == '16':
                activity16()
                continue
            elif choose == '17':
                activity17()
                continue
            elif choose == '18':
                activity18()
                continue
            elif choose == '19':
                activity19()
                continue
            elif choose == '20':
                activity20()
                continue
            elif choose == '21':
                activity21()
                continue
            elif choose == '22':
                activity22()
                continue
            elif choose == '23':
                activity23()
                continue
            elif choose == '24':
                activity24()
                continue
            elif choose == '25':
                activity25()
                continue
            elif choose == '26':
                activity26()
                continue
            elif choose == '27':
                activity27()
                continue
            elif choose == '28':
                activity28()
                continue



                
            elif choose == 'a':
                code_challenge1()
                continue
            elif choose == 'b':
                code_challenge2()
                continue
            elif choose == 'c':
                code_challenge3()
                continue
            elif choose == 'd':
                code_challenge4()
                continue
            elif choose == 'e':
                code_challenge5()
                continue
            elif choose == 'f':
                code_challenge6()
                continue
            elif choose == 'g':
                code_challenge7()
                continue
            elif choose == 'h':
                code_challenge8()
                continue
            elif choose == 'i':
                code_challenge9()
                continue
            elif choose == 'j':
                code_challenge10()
                continue
            elif choose == 'k':
                code_challenge11()
                continue
            elif choose == 'l':
                cod_challenge12()
                continue
            elif choose == 'm':
                code_challenge13()
                continue
            elif choose == 'n':
                code_challenge14()
                continue
            elif choose == 'o':
                code_challenge15()
                continue
            elif choose == 'p':
                code_challenge16()
                continue
            elif choose == 'q':
                print("system exit")
                break
            else:
                print("invalid choice")