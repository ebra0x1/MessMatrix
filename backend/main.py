import random
creds = open("creds.txt", "r").readlines()
chars = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
         'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
         'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}


def login():
    print('Hello Please Login!')
    username = raw_input("What's your username?: ")
    for x in creds:
        usrName = x.split(':')
        if username is usrName[0]:
            print(' Wants to login!')


login()

def loginTwo():
#step 1 show a enter password text
    print("Please Enter Username")
    #step 2 allow user to enter username
    username = raw_input("Enter Username Here: ")
#  have code read the username
    for x in creds:
        TheUsrname = x.split(":")
        if username == TheUsrname[0]:
            print ('Welcome')
        else:
            print('User Does Not Exist..')
#now create the Mess Matrix
def messMatrix(password):
# have the matrix loop through the chars
    random = random.randint(0,15) + len(password)
    





loginTwo()
