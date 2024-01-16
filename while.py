    """
    ******psudeo code*****
    The program will take integer from user as a input 
    while loop will stop  if user enter -1
    The entered number will be added into a variable
    Count will calculate the number entered number
    average variable used to save the average
    The average will display to the user at the end of program
    """
    # Four variable are declared with 0 to perform some function after
number = 0
add = 0
average = 0
count = 0 

# While loop is executed till number entered by user not equal to 1
while number != -1:
    # input function is used to take input from the user and store into 'number' variable
    number=int(input("Please enter an integer, -1 will exit the loop"))
    
    #the number entered by the user will be added and store into a variable
    add += number
    
    #count variable will count how many time loop is executed
    count +=1
# Here addition of all number devide by count to find the average 
average = add / count
# print function is used to print the average of all number
print("The average of all entered number is" , average)
