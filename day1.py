print('start day 1');

a = 5
print("a is ", a)

# update existence 
a = 8
print("a is ", a)

# get from user integer value
age = int(input('Enter your age  '))
print("your ag is ",age)

# get from user integer value
price = float(input('Enter price  '))
print("your is ",price)

# get from user string  value
name = input('Enter Your Name ')
print("Your Name is ", name)


# get age is odd or even
if(age % 2 == 0):
    print("your age is even")
else :
    print("your age is odd")    


# get 1 to 5 multiplication with age
for i in range(1,6):
    a = i * age
    print("i * age ", a)

# set price 5 to 1 qty
for i in  range(5,0,-1):
    a = price * i
    print("price with qty", a)
    
# get 6 to 10 multiplication with age  using while   
i = 1
while i<=10:
    if(i == 2):
        print("i is ", i)
    elif(i == 3):
        print("i is ", i)    
    else :
        print("")    
    i=i+1