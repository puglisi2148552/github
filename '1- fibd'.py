'1- fibd'

def mortal_fibonacci(n, m):
    # Initialize a list where each index represents the number of rabbits of that age
    rabbits = [0] * m
    rabbits[0] = 1  # Start with one immature pair

    for month in range(1, n):
        # Newborn rabbits are produced by all mature rabbits (those with age > 0)
        newborns = sum(rabbits[1:])
        
        # Shift age: oldest die off (rabbits[m-1] are removed), others age by 1 month
        rabbits = [newborns] + rabbits[:-1]

    # Total rabbits is the sum of all age groups
    return sum(rabbits)


n = 92  # total months
m = 19 # lifespan in months
print(mortal_fibonacci(n, m))  
