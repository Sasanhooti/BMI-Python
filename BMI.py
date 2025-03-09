def bmi():
    number_1o = int(input("Enter your the weight  : "))
    number_2o = int(input("Enter your the height  : "))
    x = (number_2o / 10)
    b = (x**2)
    output_number = (b / number_1o)
    print(output_number)
    print("If it is below 18.5, the person is losing weight.◾ Between 18.5 and 24.9, a person is in a healthy weight range.◾ Between 25 and 29.9, the person is overweight.◾ Between 30 and 39.9, a person suffers from excessive obesity.")
    
    
    again()
# Define again() function to ask user if they want to use the calculator again
def again():
    # Take input from user
    calc_again = input('''
    Do you want to bmi again?
    Please type Y for YES or N for NO.
    ''')
    # If user types Y, run the bmi() function
    if calc_again.upper() == 'Y':
        bmi()
    # If user types N, say good-bye to the user and end the program
    elif calc_again.upper() == 'N':
        print('See you later.')
    # If user types another key, run the function again
    else:
        again()
# Call bmi() outside of the function
bmi()
        
