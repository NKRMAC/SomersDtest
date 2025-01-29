import scipy

def manual_somers_d(x, y):
    # Initialize counts
    C = 0
    D = 0
    T_Y = 0

    # Calculate concordant, discordant pairs and ties in X and Y
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            if x[i] < x[j] and y[i] < y[j]:     # Concordant
                C += 1
            elif x[i] > x[j] and y[i] > y[j]:   # Concordant
                C += 1
            elif x[i] < x[j] and y[i] > y[j]:   # Discordant
                D += 1
            elif x[i] > x[j] and y[i] < y[j]:   # Discordant
                D += 1
            elif y[i] == y[j] and x[i] != x[j]: # Ties in Y (but not in X)
                T_Y += 1

    # Calculate Somers' D
    return (C - D) / (C + D + T_Y)

x =  [1,2,3,4,5]
#y = [0,1,0,1,1]
y = [1,3,3,5,4]

print(manual_somers_d(x, y)) # Correct
print(manual_somers_d(y, x)) # Reverse

print(scipy.stats.somersd(x, y).statistic) # Correct
print(scipy.stats.somersd(y, x).statistic) # Reverse
