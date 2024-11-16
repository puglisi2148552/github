'10- splc'

def parse_fasta(fasta_data):
    """Parse FASTA formatted input and return a list of sequences."""
    sequences = []
    current_seq = []
    for line in fasta_data.strip().splitlines():
        line = line.strip()
        if line.startswith(">"):
            if current_seq:
                sequences.append("".join(current_seq))
                current_seq = []
        else:
            current_seq.append(line)
    if current_seq:
        sequences.append("".join(current_seq))
    return sequences

def remove_introns(dna, introns):
    """Remove each intron from the main DNA sequence."""
    for intron in introns:
        dna = dna.replace(intron, "")
    return dna

def transcribe(dna):
    """Transcribe DNA to mRNA (replace T with U)."""
    return dna.replace("T", "U")

def translate(mrna):
    """Translate mRNA sequence to a protein sequence using the genetic code."""
    codon_table = {
        'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
        'UAU': 'Y', 'UAC': 'Y', 'UAA': 'Stop', 'UAG': 'Stop',
        'UGU': 'C', 'UGC': 'C', 'UGA': 'Stop', 'UGG': 'W',
        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }
    protein = []
    for i in range(0, len(mrna) - 2, 3):
        codon = mrna[i:i+3]
        amino_acid = codon_table.get(codon, 'Stop')
        if amino_acid == 'Stop':
            break
        protein.append(amino_acid)
    return ''.join(protein)

# usage
if __name__ == "__main__":
    # FASTA data string input
    fasta_data = """>Rosalind_0299
ATGCAATCTCTTCTCGAACTTGCACGATAACCCACCTACTGCGTACAATGCGCACGTATC
CCCACCCCTAATATTGAGACTAAGCCTGACGCTTCACGTTGCCCAGACCTCAATAATCTG
CAGGCTCGCTCGTGTATACTGGGACAACTCAAGGGTTATTATGGGACGGGGAGTCTGAAG
TTAGCACTCAGAGACCCCGTACCTCAGCATAGCCCCATGAGGAAGAGGCATGCGCCGCAT
GCTTGTCAGGCCGGCCCTCGAGATTCTATCAACCCCCAGAGGATTTTGCCCGCCGAGGCT
GTCCAGCCTATCTGCATTCAGTGGATCCATCCCGTGCCCGGCTAAACCAGCACAGTGTCC
AGCAGAGAGAACGCACAAGTGCCCCTTGTCCAACGGTCCTACAATTGTCCGCTTTCGACT
GGGGCTAGTGCCATTCTTTTCTGTTACGGACTCACAGCGGTATGGGGACTCAACTCGTCA
TCAAAGACCCTACCCACGTTCTATTCTATCCAATGGGACCGAGCAGGAGCACCAATTATT
TATTCAAGGCATCACTCTCAGGCTATTAGGCGCTACGCTCAGCACACACCAAAGTAGGTC
TGTGCGTCGACTGCTTGTAGCTCCTACGGCCCTACAGCACACGGTCGAGAGATCGATGGG
TCTCAAACAGAAATAAAATATTGGTGCGAACGAGGTGACCTTCTGAGCCTCGCAGTAACA
AATTGCTGTTGGGAGCACTGCATGGAATAGACATTTAGGGCACGGATCCGCTCACGATTT
TTTTCTCTCTCGATAGACACAAGGGCCCGGAGGCTTTAAGCTACGCTAAAGATGTATCCG
ATAGGCGCAGTAGAAAAGAGACTTCCAATGAGCCCCAGTCCCAATGCTCACTCAGCTGAG
GGGTACCTAGGTTGTCCTGCATCTCCACTGGTTAG
>Rosalind_5660
TAGCCCCATGAGGAAGAGGCATGCGCCG
>Rosalind_4405
GCCGAGGCTGTCCAGCCTATCTGCA
>Rosalind_4519
AATCTGCAGGCTCGCTCGTGTATACTGGGACAACTCAAGGG
>Rosalind_2759
TTTCTCTCTCGATAGACACAAGGGCCCGGAGGCTTTAAGCT
>Rosalind_5729
TAACCCACCTACTGCGTACAATGCGCACGTATCCCCACCCCTAAT
>Rosalind_3671
CCGGCTAAACCAGCACAGTGTCCAGCAGAGAGAACGCACAAGTGCCCCT
>Rosalind_1118
TCGATGGGTCTCAAACAGAAATAAAATATTGGTGCGAACGA
>Rosalind_2134
TGGGGCTAGTGCCATTCTTTTCTGTTACGGACTCACAGCGGTATGGG
>Rosalind_7216
GAGCACTGCATGGAATAGACATTTAGGG
>Rosalind_3478
CCAAAGTAGGTCTGTGCGTCGACTGCTTGTAGCTCCTACGGCCCTACAG
>Rosalind_3774
CAGGAGCACCAATTATTTATTCAAGGCATCACTCTCAGGCTATTAGGCGC
>Rosalind_0176
CCAATGAGCCCCAGTCCCAATGCTCACTCAGCTGA
"""

    # Parse the FASTA data
    sequences = parse_fasta(fasta_data)
    main_dna = sequences[0]   # First sequence is the main DNA sequence
    introns = sequences[1:]   # Remaining sequences are introns

    # Remove introns from the main DNA sequence
    exons = remove_introns(main_dna, introns)
    
    # Transcribe the exons to mRNA
    mrna = transcribe(exons)
    
    # Translate the mRNA to a protein sequence
    protein = translate(mrna)
    
    print(protein)
