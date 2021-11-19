#This program will help users with two different financial calculations for investment or bond.
#The program will help the user calculate the total amount including interest in their investment or the monthly repayment amount for their bond.
#The user has to select investment or bond to choose which calculation is suited for them.
import math

financial_calculator = input("""Choose either 'investment' or 'bond' from the menu below to proceed:\n
investment    - to calculate the amount of interest you'll earn on interest\nbond          - to calculate the amount you'll have to pay on a home loan:  """).lower() 
#this section will calculate the user's total investment plus interest.
#I asked the user to input all the details that we will need to calculate the total amount.
#i used the given formula to calculate both the simple and compound interest.
if financial_calculator == "investment":
    principal_amount = float(input("Please enter the amount you are depositing: "))
    interest_rate = float(input("Please enter the interest rate: "))
    interest_rate = interest_rate / 100
    years = int(input("Please enter the number of years you plan on investing: "))
    interest = input("Please select which type of interest do you prefer (simple or compound): ").lower()
    if interest == "simple":
        A = principal_amount*(1+interest_rate*years)
        print("Total amount plus interest: R",round(A,2))
    else:
        if interest == "compound":
            A = principal_amount* math.pow((1+interest_rate),years) 
            print("Total amount plus interest: R",round(A,2))
#I used the bond calculator formula to calculate the monthly bond repayment. 
elif financial_calculator == "bond":
    present_value = float(input("Please enter the present value of the house: "))
    interest_rate = float(input("Please enter the interest rate: "))
    i = (interest_rate / 100)/ 12
    months = int(input("Please enter the number of months you plan to repay the bond: "))
    x = (i*present_value*((1+i)**months))/(((1+i)**months)-1)
    print("Total monthly repayment: R",round(x,2))
else:
    print("Incorrect input!!!\nPlease run the program again and enter either 'investment' or 'bond')") 


#reference: the formula that was given for the bond calculator on the task was giving me countless errors.
#I went on the internet to search for a different formula which worked perfectly with my code.
