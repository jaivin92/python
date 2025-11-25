import math

# palindrome
# fibonaci
# reverse
# primenumber

num = int(input('Enter a number =>  '))
temp = num
rev = 0
while (num > 0) :
    digit = num % 10
    rev = rev *10 + digit
    num = math.floor(num/10)

print("rev", rev, 'num is ', temp)    

if rev == temp :
    print("given number is palidrome")
else :
    print("Not palidrome")

def isPrimeNumber (num) :
    for i in range(2, num):
        # print(i, " temp ", num)
        if (temp % i == 0) :
            return True
    return False    

if isPrimeNumber(temp) :
    print(f"{temp} is prime number")
else :    
    print(f"{temp} is not prime number")
