import math
#Gives the user the options to choose from
menu_option1 = print("Investment - to calculate the amount of interest you'll earn on your investment")
menu_option2 = print("Bond - to calculate the amount you'll pay on a home loan")

#Allows the user to input their option
menu_input = input("Enter either Investment or Bond from the menu above to proceed:")


#First step of the options would be "Investment or Bond"
#"Investment" would be followed by a few questions where it would allow the user to input an answer
if (menu_input.lower() == "investment"):
    investment = amount = int(input("What is the amount you would like to deposit?"))
    investment = interest_rate = int(input("What is the interest rate?"))
    investment = years = int(input("How many years are you planning on investing?"))
    
#"Bond" would be followed by a few questions where it would allow the user to input an answer
elif (menu_input.lower() == "bond"):
    bond = amount = int(input("What is the value of the house?"))
    bond = interest_rate = int(input("What is the interest rate?"))
    bond = years = int(input("Over how many months would you like to repay the bond?"))

#The calculations of the bond option
Value = amount
i = ((interest_rate/100) / 12)
n = years
bond_repayment = round((i * (Value))/(1 - i)**(-n))

#The calculations of the investment option
p = amount
r = ((interest_rate) / 100)
t = years
simple_calc = round(p * (1 + r*t) + p)
compound_calc = round(p * math.pow((1+r) , t) + p)

if(menu_input == "investment"):
    interest_input = input("Would you prefer Simple or Compound Interest?")

#The investment option has a sub-option which allows the user to input "Simple" or "Compound"
if (interest_input == "SIMPLE"):
    interest_input = simple_calc
elif (interest_input == "COMPOUND"):
    interest_input = compound_calc

#Prints the final answer after all options and calculations
if (menu_input == "investment" and menu_input == "investment"):
   print(f"Your total amount after investing would be R{interest_input}")
elif (menu_input == "bond"):
    output_bond = print(f"Your monthly repayments would be R{bond_repayment}.")
