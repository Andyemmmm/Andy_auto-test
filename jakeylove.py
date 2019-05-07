for i in range(6):
    for j in range(0,6 - i):
        print (end="  ")
    for k in range(6 - i,7):
        print (" *",end="  ")
    print ()
for i in range(6):
    for j in range(0,6 - i):
        print(end="  ")
    for k in range(6 - i,7):
        print (" *",end="  ")
    print()
for i in range(7):
    for j in range(12):
        if j == 7 or j == 6:
            print(" *",end="")

        else:
            print ("  ",end="")
    print()
print("="*50)