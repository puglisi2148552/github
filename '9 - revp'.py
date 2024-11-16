'9 - revp'

def parse_fasta(fasta_data):
    """Parse FASTA formatted input and return the DNA sequence."""
    current_seq = []
    for line in fasta_data.strip().splitlines():
        line = line.strip()
        if not line.startswith(">"):
            current_seq.append(line)
    return ''.join(current_seq)

def is_reverse_palindrome(seq):
    """Check if a given sequence is a reverse palindrome."""
    # Define a mapping for complementary bases
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    # Generate the reverse complement
    reverse_complement = ''.join(complement[base] for base in reversed(seq))
    return seq == reverse_complement

def find_reverse_palindromes(dna, min_length=4, max_length=12):
    """Find reverse palindromes in the DNA string."""
    results = []
    for length in range(min_length, max_length + 1):
        for start in range(len(dna) - length + 1):
            substring = dna[start:start + length]
            if is_reverse_palindrome(substring):
                # Record the position (1-based) and length of the palindrome
                results.append((start + 1, length))  # start + 1 for 1-based index
    return results

if __name__ == "__main__":
    # FASTA data
    fasta_data = """>Rosalind_1098
CGCGTAGCTTCGACTTTTTAGCGGTCAATGGAATGAAGAGCACGTCCGGGGTCTGAATCT
TTCGAGCGTGAATTTTTCTCGTCGCCTCCCTTTAGATTTCTCAGACTTCCAGATCCCGAC
TAATAAAGTAGTGTAATGACACGTCTGACTGGTGGACAGCGCGCGTTGGCAAGGCCGTGG
CGTAACAGGCTACCCACTTACAGTAGGGGATATGACTATATCCCGACGTAAATGTCATGC
CTGGGGGACTGGTAATTAGCCTAACCGCGATGATATTCTCCAGTTGTCCCAAGGATGACG
CCGCCCACGCGTAGCTCGATGTGAAGGCTGGTTACCAAGGTATTCTAAAATTTTAACCGG
GCAGCCCTTGAGAATCAGATCAAGGACTACACCCTCCAGGCGTCGTCCACATGGCAGTGC
GTTCGCGGATAGCGTGCTGCACATAGCTCAGACTATTCGCTCCCGGAAACTAGCTAGTTC
GAGCAGCAACGTCAAAGTCAGTCTTAAAGGTGCTGATTTGGAGTCGTCGCCACCCTCAGG
AAGCTAGGTCATTAATAACCCATTTCGGGCCTATAACCGAGCGAAATCGGGCTTGTGAAC
GAGCCTCCGGATGGTAGGCTTCACTCCGTGGCATCGGCCACGATGACAGGGCATCCCCCT
AGAGTGTCCAGTATATGATCATGTAAGACCCTCAAGTAAGATCCATTGTCAGCCTTTAAA
AATATGACACGAAGGTGAGCGCTCGCACTTGGAGGCGCTCCTACTTTACTTTAGTATGTG
CACACATTCTCACACCAATCCCTCACCAGCCTATCCCTGCCGCTCTAGTCCGGTGCCATA
CGGAGTTCTATGGTTCCACTCATCGGCGAACTGGATCACGAATCAGGTTCTTTGGGAACC
TAACTCTGCTTCCGCCAGAGTCCCTAACCGGCTTAAAGTTCGCGCG

"""
    
    # Parse the FASTA data
    dna_sequence = parse_fasta(fasta_data)
    
    # Find reverse palindromes
    reverse_palindromes = find_reverse_palindromes(dna_sequence)

    # Output the results
    for position, length in reverse_palindromes:
        print(position, length)
