' assignment 5 - rabbits'

def rabbit_pairs(n, k):
    # Base cases
    if n == 1 or n == 2:
        return 1
    
    # List to store the number of rabbit pairs for each month
    rabbit_population = [0] * (n+1)
    rabbit_population[1] = rabbit_population[2] = 1
    
    # Calculate the number of rabbit pairs for each month using the recurrence relation
    for i in range(3, n+1):
        rabbit_population[i] = rabbit_population[i-1] + k * rabbit_population[i-2]
    
    # Return the total number of rabbit pairs in the nth month
    return rabbit_population[n]

# Sample input
n, k = 33, 3

# Calculate and print the result
result = rabbit_pairs(n, k)
print(result)
