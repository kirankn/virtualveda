# Asking the user for principal, rate of interest and time
P = float(input('Enter the principal: '))
R = float(input('Enter the rate of interest per annum: '))
T = float(input('Enter the time in years: '))
# Calculating simple interest
SI = (P * R * T)/100
# Calculating amount = Simple Interest + Principal
amount = SI + P
# Printing the total amount
print('Amount payable:',amount)
