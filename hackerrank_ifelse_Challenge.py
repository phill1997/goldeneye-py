#Task
#Given an integer, , perform the following conditional actions:

#If  is odd, print Weird
#If  is even and in the inclusive range of  to , print Not Weird
#If  is even and in the inclusive range of  to , print Weird
#If  is even and greater than , print Not Weird


n = int(input("Enter a number: "))

if n % 2 != 0:              # check for odd number. All other numbers are even
    print("Odd Weird")      # All other numbers are even. even number between 2-5
elif 2 <= n <= 5:
    print("Low Not Weird")
elif 6 <= n <= 20:          # Even number between 6 - 20
    print('Weirdo')
else: print('Not Weird at all')  # All other even numbers greater than 20.