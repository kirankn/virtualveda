## 4. Write a program to calculate the amount payable if money has been lent on simple interest. Principal or money lent = P, Rate of interest=R% per annum and time=T years. Then Simple Interest SI=(PxTxR)/100. Amount payable=principal+SI. P,R,T are given as input to the program.

<!-- ### Flowchart
![Image](./p4.png) -->

### Program
[Download Source Code](./p4.py ':ignore')
```python
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
```

### Output

```bash
Enter the principal: 100
Enter the rate of interest per annum: 10
Enter the time in years: 2
Amount payable: 120.0
```
