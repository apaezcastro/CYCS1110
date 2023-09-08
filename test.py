#This program adds two numbers, and display the result

#New line function
def nl():
    print('\n')

# This function lets the user know what the program does
nl()

print('This program is meant to add two numbers together')

nl() #prints a space between header and programs

#Input Steps
while exit != 'no':
    num1 = int(input('Provide a number: '))

    num2 = int(input('Provide a number: '))

    results = num1 + num2

    print(results)

    exit = input('would you like to run this program again? ')

