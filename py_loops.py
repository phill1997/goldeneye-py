#!/usr/bin/env python3.7
#Author Paul Hill

# Ask for input and verify.
#Print "FizzBuzz" if the number is divisible by 3 and 5.
#Print "Fizz" if the number is divisible by 3.
#Print "Buzz" if the number is divisible by 5.
#Otherwise print the number.

#Code here

counter = 1
while counter < 3:
    upper_number = int(input("How many values should we process 1 - 100: "))
    counter + 1
    if upper_number < 0 or upper_number > 100:
        print("Sorry, you must enter a number 1 - 100")
    else: break    
            
for number in range(1, upper_number + 1):
    if number % 3 == 0 and number % 5 == 0:
        print('FizzBuzz')
        
    elif number % 3 == 0:
        print('Fizz')
        
    elif number % 5 == 0:
        print('Buzz')
        
    else: print(number)
            


    