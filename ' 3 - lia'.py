' 3 - lia'


from math import factorial

def binomial_coefficient(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

def binomial_probability(n, r, p):
    return binomial_coefficient(n, r) * (p ** r) * ((1 - p) ** (n - r))

def probability_at_least_N_AaBb(k, N):
    # Number of organisms in the k-th generation
    total_offspring = 2 ** k
    # Probability of an offspring being Aa Bb
    p_AaBb = 0.25
    
    # Calculate the cumulative probability of having fewer than N Aa Bb organisms
    cumulative_probability = 0
    for r in range(N):
        cumulative_probability += binomial_probability(total_offspring, r, p_AaBb)
    
    # Probability of having at least N Aa Bb organisms
    probability = 1 - cumulative_probability
    
    return probability


# k = 6, N = 19
result = probability_at_least_N_AaBb(6, 19)
print(result)
