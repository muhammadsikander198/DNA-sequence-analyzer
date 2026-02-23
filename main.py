# DNA Sequence Analyzer

dna = "ATGCCCTAGGCTAGCTAGGCTAATGCGT"

# Length
print("Length:", len(dna))

# Nucleotide count
print("A:", dna.count("A"))
print("T:", dna.count("T"))
print("G:", dna.count("G"))
print("C:", dna.count("C"))

# GC Content
gc_content = (dna.count("G") + dna.count("C")) / len(dna) * 100
print("GC Content:", round(gc_content, 2), "%")

# Reverse Complement
complement = dna.replace("A","t").replace("T","a").replace("G","c").replace("C","g").upper()
reverse_complement = complement[::-1]
print("Reverse Complement:", reverse_complement)
