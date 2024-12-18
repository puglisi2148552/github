' assignment 6 - gc'

def parse_fasta(data):
    fasta_dict = {}
    label = None
    
    for line in data:
        line = line.strip()
        if line.startswith('>'):
            label = line[1:]  # Remove '>' and store the label
            fasta_dict[label] = ""
        else:
            fasta_dict[label] += line  # Append the DNA string for the current label
    
    return fasta_dict

def gc_content(dna_sequence):
    gc_count = dna_sequence.count('G') + dna_sequence.count('C')
    total_count = len(dna_sequence)
    return (gc_count / total_count) * 100

def find_highest_gc_content(fasta_dict):
    highest_gc_label = None
    highest_gc_content = 0.0
    
    for label, dna_sequence in fasta_dict.items():
        gc_percent = gc_content(dna_sequence)
        if gc_percent > highest_gc_content:
            highest_gc_label = label
            highest_gc_content = gc_percent
    
    return highest_gc_label, highest_gc_content

# Sample input in FASTA format
fasta_data = [
    ">Rosalind_9684",
    "GTGGTCATGGCGAATCGGGTCCAGTCGGTTAATTTTTGTCGTTAATGGCAATTGTCGTACTGGGTCGGCTGATAGCATCCATAAGAGTCTTAGGGATTCAGCTAACTTATGCCTGAAGGCACCTCTGACGCCGTAGCCGCAACCCGCATTTTGGACGGTCGGCGAGCCTGCAAGCTCCTACACCACACAAGGACAGGCTGTAGCGACTAGGGGGCGCTTAGCGAAGAGCTGAGGCAATAAATCGTGTCTCCCTGCACTATCTGGATGATTCACATGTAAGGTACCTTACCGCTGGTGGCGCTGCCCCAGGGCTCACCAGGTTCAAATCGCCTCTTGGACACGTGCTACGGGTTTCTAAAAGCGGATATCGACTCTAAAACGATTCTACTCTGTCAAGCTACATGGATATGGCTTGAGGCCTCGTCGCAGGTCTCTTCCATTGAATATTGGAGCTGTGTAACGAAGAGCTATACGGGTTCACAGACTGGTGGCTGCTCTGTCTTCGCGAGTGCGATTTGACCCCCAAGTGTGATGTGCGCGTACGACAATCTCGGAGATCGGTAGTAATAGGGGATTACTGTCTATTGGCTCCAAAAAGGGCTCCCAAAAGAGGAAATCGCGCAGAGCTGCAAGCTCAGCGCTGATTGCGGCGGTTTTCACCGACGCGATGGTTTCCCGAGTCACTCGTATTTCGTATGTCACCACCATCGTCACAGGGGTGACGTGCGTGATCATTAGATTCGATGAGCTAGACCGGAACCGAGTGAAGTGGTAAGGCTGTTTGGGACGGACATGGGATAGTGTCACTATCTGATGTGAGACTTAATTCGGGTGAACGCCGAGTCATACACGG",
    ">Rosalind_2063",
    "GTCGGCTTTTATGCTGAAGAATGGCAACCTGCTCCTTTCTGACTCGAGACTGATGTCGCATGCGCAAGTCACCGAGTTCATTCACTGCTGCATATGGGTCCAAGCAGACCCCCGGCATACGTCCGCGGGCGAGCCGGCCTGCTATTGTGCCACACGAAGCTGAGGTCGCTGGAGCCTACTTATAATCCCGAGCATGTACTACGACAAACAACCTGCCGTAGGCACAAACTCGAGTAGCTGGTCTCACCCCTCCGAGTTTGACCTTCCCAGGCGTATGTGCGCAGCATGTTCCGGTAATAGCCACCGGGTAGGGCGGAGCGTGCAGCGGTAAAGGAGGTTTATTACCCTGTAGTATGAGTCCCACTGCGAAGGGACCAGCCTCCATCAGTAATGAGTTACCATGATACCACTCTTGCGTCCACTTAGAACCAAACTTGGTTGTTTCGAGATTATAGTCCCCCCAGAGATTGCTAGTCACCTCCATTTGATTGATTTGTGACTATCGGGCGAATAGGGGTCGCTGACACCGCATGGTTACCGGCTTACAAGAGAATTGTGTGCCAACACGCCCCCTAGAATTACGTAGGAATGTGCCGGCTCTTAGATCTTTACGCGGGAGCGCGTCCTTCAGTGCGAATTGTATAACGCACCTTAAGCGAGCAAAACAAACGCAGCGGTTATCCCAACAGGCTCCGCAGCACCCTGAGGATGGTCTACTTGGACGAGGCGATGTACACTGGTACGGTCTTTGATTTTGTACACAGCCAAACTTACAACGGAGGTTATATCGACCTTCGCGGCGGTTCTGCAACGGTGCCCCCTGTCGGTTTTACAGGCTAGCCCCCCGCTGCACACTCGAGGGTACCATTTTGGCTAGCAGGTCAGCACGCACAACGTATTTCCAA",
    ">Rosalind_0925",
    "ATGCTCAAGAAAGAAGTCACGCATGTTCAAGTAACTACTACTCTTCACATCAACTATGAGCTTATACCGTATAGGTCATGGACAGAGTTCCTGCAAGACCTCGGACCGTCGGCTCTGTCCCCGCCAGATCTAGGTGAGTCGAGCAAGTTATACGACCGATCGGATCGATCTATGGATTTATAGCATCACCCAATCGCTTCTCCCTTCGACTGTTTAACAAAGGACAGGATGAACGATCGTATGCTCCGCTTGCGAGCGAGTTTAGTGAAACGTTCATTCGTCTCCTTGCCCGGGGGGATTGCAGTGCCCGGTACTCCTTTTTTAAATACAATACTATTCGCAGTATGCATAAACAGACAACTCCCTCGCAATTTGCAATCCAGAAAAAACTCTTGAGGGTTGACATACTCCTACTACCACAACTTACCGAATACTACAGAGGCAAGAGCGCTAGATCAGTTATCTTAAGCGACCCGCCTCGTCGAACGCAGCGTAGTAGTATAAGTTTCGACACCAGTTACACACCGTAGCTCGCCGGTAGTTCCCTATTATGTGGCTCCCCTCAGCAGGGTTCGCAATAAAATGACCTTGAACGACATTTGTTTTCGAGGACTTAACAATAACGCCTGATATTGCCATTTTCTATGTATCACGTGGAGACATACCCAAGTGTTTCTATCTCAAGAACTGTAAAATTCTTATTCTCAAGTACCGGCTACCGCTTGAATTGCCAAGATTGTTTGACCTATGGGCCTAGCCACCCCACATGGCGAGATCGGGTCGTGCTTAGATAGGGTCATACGTTATGTATCCGTCTTAAGTGCACTCTCAGCCGACAACAGAAAGCTTGATGCGTGGTGCTCCGCCCAATCCACCTTTCAAGAGACTCGAAGATGGAGAGTGAATTGTCGAGTCTTATCTCACA",
    ">Rosalind_0595",
    "TGATTATCGCCCGGGTACCGCCAAGGGCTACCATGTGGTGTGTAGGGCGTGACGATTTGTAAAGTTATCAAATTTACTAGCTTTCGCAGTCTCACTCAATAGCCGATTAATTTTAGAGGATTAGCCGGCCGCTCGCCACCGTCGTCTTCTGGAGGGTCGGCTTGTTTCTTACGGCGGTTTTCAGAGTGTATCTGGAACTCAAGCTTTCAGGGCGCGGGGACGTTACACTTGCACGCGAAGGCCCTGTACTGCTTACTCCCCCTGCCGATTAGGCATAGTCAAAAATTCCCCCCAGTAATATCTTGCTTATACCTCAAGTTATAGGCGAGGGCCTACCCTGGGACAAAGATCCCGAGAACCGGCCCCGGCCCTTCGTGGGCTGCATCACTACGTTATCCTACTCCTACCTCGGCTGGGCTTGGAGATCTTCAGCCGTTCCTGGCCGCACGCCCTTCAGCCTACCCAGCGATACCACTTCATTTATACGATGTACGAGCAGGCTACTGGAGGCCGACCTTTGGTTCTTTGCTATGGCATTGAAACCATTTGAGGCGGCTGTTTGATCATCAGTAAACGGTCTAAACCCCTCCAGCCTCGAAATTCAGTTATAAATAGTCATCCCTTATCAGTTGTCCTTAGCGCAAAAAATGAAGATTACTTGCGCAAAGTAGAAAATCCATGAGGACGTAAGTCAGCTTCTCCCAGATGTATGGGGTTAGTCCGCAGAATTCCCCTGACTTCGAGTTGACTCCCGCCTATACGTTGCTGGGATGCTCATTACTCCCAACTGACTCGCGTTACTTGACTCAGTACCGCCACGGGGCGCCTTACTCTTAGGACTCTTGGGGGTTATAGGCCCCTATTATTGGCGTTTGTCGTATCGCGGCTTATAACGCAGCACCCCCACGAGAGTTGCGCCTAAAGCGGGTGGAGGTATTACACCTCAATATGCCCCTAACTCAAGTGCCCAGCAGCCAAGTTAG",
    ">Rosalind_5148",
    "TAAAGAACCAGACTGCGATGGAAGCACCCGGTTGTGTACGCAGTTTACTACGAGTTAGACAGGGTGTCGTTTTGGCTTAGTAGACATCAGACGACTTATTGGGGGCAACACCGTATGTGTCCGCTGACAGACGCTGCTTTATCGGTTGGAGGCACAGACTGCGTAACTGAGCCGGATGACATTGGACAAGACCTTAACATCGCGTGGACGCTTAACGATTTTGTGAACTCGTGCCGATAGTGTATGTCGTTGAAAACACATGAGATTACGTTACCGGACCAGCGAGAGCTTGTCACACCAGTACCTCGAGTCAAATCTGGCCGTATTTGCCATAAAGAGCATAGCAACTGCTGTCTGTGACCGCGGTCGGCAATCTGTCCCCAGAAAGGAATCATGAGCAGTTCCTATTCTTGCTGGTTGGGATAAGGCTTGTAGTTTCGCATCGCCCCAATAATTATTTTGTAGGGGAGAATTGTATATAGATGGGTATCTACCGTACACCGCAATTATAGGGGCACCTACTTATTAAAGGAAGATGTTTGATGGCCTATCACTTTGAGCTGATTAGCTTAGGGTAGTGACCTATGGTAGTTACGGAGCCGGGCACCCCTAGTCCTACTCTGCAGACGATACAGGTGGAGCTCCACCCTGAACAACACCAGTGTAAACTCAAACGTCGATGCCCCCGATAACAAGGGTCTCCGTTTCTAGAGCGTTCTGGGCGTCCTTCAGCACCTGCCAGGCTGTGAGGAACTTAGTTTCAAGCGCGGGTGCTCGTATAGGAGCAACCGACATTTGTATGGGGTATGCTTTGGCTGTCTAAGAAAAAGATCTTGAGCTGATCTACGTCAG",
    ">Rosalind_0237",
    "CTTATTGGTTCGGCTATAGAAAGATTCGTGCACGATCGGACGGTGACTGGCTATAAAAACCGAACCCTCCGATTGGGTGTAAATACCGTGGCCGAGAACATAGAGGTTTCATTACTGTACAACGCAGGTGCGTGTGAAATCACAAAGCTGTTACTACTTCAATCTCGAGCCCTGCATTTGCGTACTATTACGCGGCGCGATAGTATACGGAGCTTATCGTATCATAACAATGAGTAATGGTATTCATGCGAAGTGCGCACGTGGTTGTGCAAAGACACGACTCGTGTTTGATTCTTCTTTTATCATCAACAGCTGGTAGAGCTTTAAGGGGAGCCACCCAACTATACCGTGGCTTGCTATGTGCCTCCAGCTGCTTACAAATATACACGAGCGTTCTTCAGATGCACGCCTTTGGAGCAGCTATAGTGCTAAAGCTCTGCAAGATACCCACAACCAATCCGGTAGAGCCGACAAGCCTGAACGAAAACAGAGTGCTCCCATATCGCCCCGATTGCTGGAGAATCATGTCCTTCGATGGGCCCGCAGCTCTGAGGAAGCTTAGCAGCTTTGAGTGGAAGAAATCGAACGGTGGAGTCTCCACCTCGGTTAAGAAAGTAAGGTGCGCTGAGGTGCAGGGACAGTCAGGCCTCCCCCCCATTTACCGTTGATACAGCGTAAAAATTTCATCCGGCCGTGAGAGGAGGCTATAGCCGCGTCCCTGCAAGATGCGGCGATTAAACATTGTCTTTACTTTTACAACTATTGCAATTGATGACAGGGCTGTCTTTGAGGGCAATGTATTGACAAATAAAACTTACAGGGCGGAAGTGAACATGTACTGCCGCACGCACATCCCCTCCAGAAGGTCAGTTTGCCGTGTCAGAATGGAGGTCATCCTACGGTGTCTTGCTGCTAACGGAGTGGCCGAACCGTTTTGCCTGTTTCTTTCAACTTGGCCGTTTATAGATGAGGGAAGTAGCCTCCGAGA",
]

# Parse the FASTA data
fasta_dict = parse_fasta(fasta_data)

# Find the label with the highest GC content
highest_gc_label, highest_gc_content = find_highest_gc_content(fasta_dict)

# Print the result
print(highest_gc_label)
print(f"{highest_gc_content:.6f}")
