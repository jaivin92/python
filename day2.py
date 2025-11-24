print("Day 2 code learn funciton  def, lamda and pattern")

for i in range(1, 5):
    for j in range(1, 5):
        print(" * ", end="")
    print("")    


print("Pattern 2")
for i in range (1, 5):
    for j in range (i, 5):
        print(" * ", end='')
    print("")    



print("Pattern 3 right side")
for i in range (1, 6):
    for j in range (1, 6-i):
        print("   ",end="")
    for k in range (1,i):
        print(" * ",end="")
    print("")    


print("pattern 4 left side")
for i in range (1 ,6):
    for j in range (1, i):
        print(" * ", end="")
    print("  ")    

def isOddNumber (n):
    if(n % 2 == 0):
        print("this is even", n)
    else:
        print("this is odd", n)    


isOddNumber(5)
# print(isOddNumber(5))

add = lambda a,b:a+b
test = add(5,20)
print(test)


