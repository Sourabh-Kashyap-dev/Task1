
# 1. Addition of 2 numbers given by user
x = input("Type a number: ")
y = input("Type another number: ")
sum = int(x) + int(y)
print("The sum is: ", sum)





# 2. to check number is even or odd 
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))






# 3. to find the factorial of a number 

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
num = int(input("Enter a number: "))
# Checking if the input is valid
if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0:
    print("Factorial of 0 is 1")
else:
    result = factorial(num)
    print("Factorial of", num, "is", result)








# 4.  to find Fibonacci sequence 

#first we will set first two values of fibonacci series:
a=0
b=1

#give number of terms of fibonacci series you want to print
n=int(input("Enter the number of terms of fibonacci series:/t"))

if n==0:
   print(a)
elif n==1:
     print(a)
     print(b)
else:
   print(a)
   print(b)
   for i in range(2,n):
       c = a + b
       print(c)
       a = b







# 5. to reverse a string

# Take input from the usertext = input("Enter a string: ")# Reverse the stringreversed_text = text[::-1]# Display the resultprint("Reversed string:", reversed_text)







# 6. palindrome checker
# Take input from the user
text = input("Enter a string: ")

# Convert to lowercase for case-insensitive comparison
text = text.lower()

# Check if the string is equal to its reverse
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")








# 7. leap year checker
# Take year input from the user
year = int(input("Enter a year: "))

#  Check leap year condition
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")









# 8. to find number is armstrong or not

# Take input from the user
text = input("Enter a string: ")

# Convert to lowercase for case-insensitive comparison
text = text.lower()

# Check if the string is equal to its reverse
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
