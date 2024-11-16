'2 - mrna'

def count_mrna_sequences(protein):
    # Codon counts for each amino acid
    codon_count = {
        'F': 2, 'L': 6, 'I': 3, 'M': 1, 'V': 4,
        'S': 6, 'P': 4, 'T': 4, 'A': 4, 'Y': 2,
        'H': 2, 'Q': 2, 'N': 2, 'K': 2, 'D': 2,
        'E': 2, 'C': 2, 'W': 1, 'R': 6, 'G': 4,
        'Stop': 3  # Stop codon possibilities
    }

    # Start with the stop codon count since every protein sequence ends with a stop codon
    total_count = codon_count['Stop']

    # Multiply by the number of codon options for each amino acid in the protein
    for amino_acid in protein:
        total_count = (total_count * codon_count[amino_acid]) % 1_000_000

    return total_count


protein = "MPHLQQPVKTFIMQCFHFIHQTHTLVTARVKSGKPYCVAEQIFKTQQLIGAVRGDIHFNPEYSNHWKKGAQAALVVNSECINQFPNGMGMIRRLFAYNWYSVETTTFVKYRKGPCDFINNACNCLDELEIIGSSIHFSIEYWLTFGVYICKNTWTYQGHLYESHNMRKWMSVMHHLPAYPQMCDYIKVCKYCISDKWCGPWMVCHFHCATGFNCRSHWTAWYFYEKDVKFDDENRDRATPENSSWSAPRVLMVLRVRHINDCSIGAFPDMGINQQMHIFATYQTTMDGTRGMTTGHPIVFKNNADAMAWVRIMAMPNYFPNIRAYNIMQHIFYPIHRVPNKVCVRMSIRFVCVSERNNVYQFAVHKSLASCVRRQPYYKAGPVANHNVTCLLHPCYFMSLNHMGFPAEKVENRGICDAAANIHTWHNAGEMWFVTHNHRFLDEREKQWCNQGKAQTCDMAFKDEIAYQVNTVQKCTSNYPSCNGHEFTHDCMHMSDDRGDNQMTQFMSARCQSSTHHTACTNAWFSHGFQAGWHEQSSNLSINPLVEVDILSIQPELMRMYLYSYDTTSIHKRFDYWFFHVNCIVQGPSTHLNPIYVNQHAIQLHENHFEMTAQNTYEVLQMMGHVKWHIHLSSVYEPPNCYSAAEYNMTQKGLCLCCVSRNMNEWQGCIGGACRFNKHWGPDEVSVSWDFMQNQVSNINRRLKLDMTSFSTMFEWKTPCYCAMYWPYFFHLMLDRWIIFTQRATVAAMDCQWTVQCSQWHLGYVLDSMSHIMFRMFADMMDYYNYGHQRNTDYNPTHICWCAECYGTHSSAHTKCPQHLWIMHYDAPHFDTFPIVSPEVDQHEHGMIALDTMFENDSLEDIILKEPNENVNPTYGYLQEALPDDAWNVAWMRKPMYMIAGNHCRRCEDGLVFGVYMWSHKFLGQQNGQMITEWALYIDWNNIIRRTSDPGDLWHFRTVLEDVSLNFAGKWIMGLAKVIYLDARCTKSGCQWQAPFPQ"  # Replace with your protein sequence
print(count_mrna_sequences(protein))  # Output will be the count of possible mRNA sequences