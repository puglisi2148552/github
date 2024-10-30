' assignment 4 - mendel laws'

def dominant_phenotype_probability(k, m, n):
    # Total number of organisms
    total = k + m + n
    
    # Total possible pairings (selecting two individuals)
    total_pairs = total * (total - 1)
    
    # Probabilities of dominant phenotype from each pairing
    prob_dominant = 0
    
    # Pairings: AA x AA, AA x Aa, AA x aa
    prob_dominant += k * (k - 1)               # AA x AA -> Always dominant
    prob_dominant += 2 * k * m                 # AA x Aa -> Always dominant
    prob_dominant += 2 * k * n                 # AA x aa -> Always dominant
    
    # Pairings: Aa x Aa, Aa x aa
    prob_dominant += m * (m - 1) * 0.75        # Aa x Aa -> 3/4 chance dominant
    prob_dominant += 2 * m * n * 0.5           # Aa x aa -> 1/2 chance dominant
    
    # Calculate probability of producing dominant phenotype
    return prob_dominant / total_pairs

# Sample input
k, m, n = 18, 18, 25


# Calculate the result
result = dominant_phenotype_probability(k, m, n)

# Output the result
print(f"{result:.5f}")
