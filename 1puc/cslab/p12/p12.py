n = 5
for i in range (n, 0, -1):
    # The space will increase on each iteration as i value will decrease
    space = (n - i)*" "
    #uncomment the below line if you wish to print as an inverted funnel
    #print(space, end=" ")
    #This for loop will print the increasing numbers
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
