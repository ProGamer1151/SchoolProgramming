import time
print("Q8 done correctly.")
print("Is it a vertebrae? If yes then enter 0 if yes- then enter 0 and if not, then enter 1.")
check1 = int(input())
if check1 == 0:
    print("Does it have wings? If yes then enter 0 if yes- and if not, then enter 1.")
    check2 = int(input())
    if check2 == 0:
        print("It's a Bird!")
        time.sleep(2)
        exit()
    else:
        print("It's a mammal!")
        time.sleep(2)
        exit()
else:
    print("Does it need water in it's habitat? If yes then enter 0 and if not, then enter 1.")
    check3 = int(input())
    if check3 == 0:
        print("Does it have fins? If yes then enter 0 and if not, then enter 1.")
        check4 = int(input())
        if check4 == 0:
            print("It's a Fish.")
            time.sleep(2)
            exit()
        else:
            print("Well, I don't know. Seems alien to me.")
            time.sleep(2)
            exit()
    else:
        print("It's an amphibian.")
        time.sleep(2)
        exit()

