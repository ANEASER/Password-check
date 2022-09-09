import string
import random


# Bug fixed

n = 1
N = int(input("Enter the password count : "))

def checkSP(p):
    SPchars = ["#", "@", "*", "&"]
    i = 0
    while i < len(p):
        if str(p[i]) in SPchars:
            return True
        else:
            i = i +1
    return False


def check_AaD(p):
    UPIN = any(i.isupper() for i in p)
    LOIN = any(i.islower() for i in p)
    DIIN = any(i.isdigit() for i in p)
    M = checkSP(p)

    if len(p) >= 7 and UPIN and LOIN and DIIN == True and M == True:
        print("Accept Password")
        print(p)

    else:
        if UPIN == False:
            p = ADD_UPPER(p)
        if LOIN == False:
            p = ADD_LOWER(p)
        if DIIN == False:
            p =  ADD_DIGIT(p)
        if M == False:
            p = ADD_Special(p)
        if len(p) < 7:
            Final = ADJUST_Length(p)
            return Final
        else:
            return p




def ADD_UPPER(p):
    AlPI = list(string.ascii_uppercase)
    r = random.choice(AlPI)
    p = str(p) + str(r)
    return p

def ADD_LOWER(p):
    alpi = list(string.ascii_lowercase)
    r = random.choice(alpi)
    p = str(p) + str(r)
    return p

def ADD_DIGIT(p):
    digis = list(range(0,10))
    r = random.choice(digis)
    p = str(p) + str(r)
    return p


def ADD_Special(p):
    SPchars = ["#", "@", "*", "&"]
    r = random.choice(SPchars)
    p = str(p) + str(r)
    return p

def ADJUST_Length(p):
    while len(p) <= 7:
        func_list = [ADD_DIGIT,ADD_Special,ADD_LOWER,ADD_UPPER]
        for func in range(4):
            p = random.choice(func_list)(p)
    else:
        return p

# --------------------------------------------------------------------------------------
def main():
    char_count = int(input("Enter the charactor count of the password : "))
    pword = input("Enter the preferred password : ")

    if  char_count == len(pword):
        pp = check_AaD(pword)
        return pp
    else:
        print("charactor count not matching...")

# ---------------------------------------------------------------------------------------
pwordlist = []
while n <= N :
    x = main()
    pwordlist.append(x)
    n = n + 1
else:
    print("END...")
    for i in pwordlist:
        print(i)
