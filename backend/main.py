import random

creds = open("creds.txt", "r").readlines()
chars = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
         'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
         'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}


def login ():
    print('Hello Please Login!')
    username = input("What's your username?: ")
    for x in creds:
        usrName = x.split(':')
        if username == usrName[0]:
            if messMatrix(usrName[1]) == True:
                print('Successfull Login!')
            break
        else:
            print('User does not exist')

def messMatrix(password):
    lengthOfPassword = len(password)
    numCorrect = 0
    while numCorrect < lengthOfPassword - 1:
        randNum = random.randint(0,1)
        if randNum == 0:
            #with password char
            answer = printMatrice(password[numCorrect], 0)
            if answer == 'No':
                print('Wrong!')
                break
            elif answer == 'Yes':
                numCorrect = numCorrect + 1

        elif randNum == 1:
            #without password char
            answer = printMatrice(password[numCorrect], 1)
            if answer == 'Yes':
                print('Wrong!')
                break
            elif answer == 'No':
                pass

    if numCorrect == lengthOfPassword - 1:
        return True
    else:
        return False



def printMatrice(passwordChar, randNum):
    if randNum == 0:
        print("\n Is your password char in this matrice?\n")
        putPasswordCharIn = False
        for x in range(0,3):
            list = [random.randint(0,9), random.randint(0,9), random.randint(0,9)]
            if random.randint(0,1) == 0 and putPasswordCharIn == False | (x == 3 and putPasswordCharIn == False):
                list[random.randint(0,2)] = passwordChar
                putPasswordCharIn = True
            print(list[0], list[1], list[2])
        return input("\n[Y]es or [N]o?: ")
    elif randNum == 1:
        print("\n Is your password char in this matrice?\n")
        print("N|N|N")
        print("N|N|N")
        print("N|N|N")
        return input("\n[Y]es or [N]o?: ")





login()
