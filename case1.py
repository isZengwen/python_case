for i in range(0,5):
    for j in range(0,5):
        print("* ",end="")
        if (j+1)%5 == 0:
            print()

print("-"*6)

for i in range(0,4):

    for j in range(0,5):
        if i ==0 or i ==3 or (i == 1 and j==0) or (i == 1 and j==4) or (i == 2 and j==0) or (i == 2 and j==4)  :
            print("* ",end="")
        else:
            print("  ",end="")
    print()



print("-"*6)


for i in range(0,5):
    print("* "*(i+1))


print("-"*6)


for i in range(0,5):
    for j in range(0,5):
        if (j ==0) or (j ==i) or (i ==4):
            print("* ",end="")
        else:
            print("  ",end="")
    print()

print("-"*6)

for i in range(0,5):
    print("* "*(5-i))

print("-"*6)

for i in range(0,5):
    for j in range(0,9):
        if j in range(4-i,4+i+1,2):
            print("*",end="")
        else:
            print(" ",end="")
    print()