# Two finance calculators (investment and bond)

import math

print("Investment- amount of interest you'll earn on your investment.")
print("Bond- amount of money you'll have to pay on your home loan")

# user must select which financial calculator they wish to access.
calc = input('Enter either "investment" or "bond" to proceed:').strip().lower()
# request required inputs: principal amount, interest rat, years.
# Pi(principal amount), ai(total return), ri(interest rate),and ti(years).
if calc == "investment":
    Pi = int(input("Please enter the amount you would like to invest in R:"))
    ri = int(input("Please enter the interest rate in %:"))
    ti = int(input("Please enter the number of years you plan to invest:"))
    interest = input('Enter either "simple" or "compound":').strip().lower()
# User must select simple or compound interest, calculate total returned.
    if interest == "simple":
        ai = Pi*(1+ri/100*ti)
    elif interest == "compound":
        ai = Pi*math.pow((1+ri/100), ti)
    print("Your investment will be worth R"+str(ai))
# If the bond caltulator is selected, request the cost, tearm and interest rate
# pb (initial cost), ib(interest in months), and nb(number of repayment years).
elif calc == "bond":
    pb = int(input("Please enter the present value of the house in R:"))
    ib = int(input("Please enter the interest rate in %:"))
    nb = int(input("Please enter the number of years to repay the bond:"))
    monthly_rate = ib/12
    total_months = nb*12
# calculate using the bond formular and return total repayment to the user.
# convert interestrate and number of years to months.
    repayment = (monthly_rate/100*pb)/(1-(1+monthly_rate/100)**(-total_months))
    print("Your bond repayment is" + " " + "R"+str(repayment))
# if the user does not select "bond" or "investment", return the error message.
else:
    print("invalid input, please type in investment or bond.")