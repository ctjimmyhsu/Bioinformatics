# DNA Toolset/Code Testing File
from DNAToolkit import *
from utilities import *
import random

rndDNAStr = ''.join([random.choice(Nucleotides) for nuc in range(50)])

DNAStr = validateSeq(rndDNAStr)
result = countNucFrequency(DNAStr)

print(f'\nSequence: {colored(DNAStr)}\n')
print(f'[1] + Sequence Length: {len(DNAStr)}\n')
print(colored(f'[2] + Nucleotide Frequency: {countNucFrequency(DNAStr)}\n'))
#print(' '.join([str(val) for key, val in result.items()]))
print(f'[3] + DNA/RNA Transcription: {colored(transcription(DNAStr))}\n')

print(f"[4] + DNA String + Reveerse Compliment:\n5' {colored(DNAStr)} 3' ")
print(f"   {''.join(['|' for c in range(len(DNAStr))])}")
print(f"3' {colored(reverse_complement(DNAStr))} 5'\n")

print(f"[5] + GC Content:\n {gc_content(DNAStr)}%\n")
print(f"[6] + GC Content in subsection k=5: {gc_content_subsec(DNAStr,k=5)}\n")

# Storing File contents in a list
FASTAFile = readFile("gc_content.txt")
# Dictionary for labels + Data
FASTDict = {}
# String for holding the current label
FASTLabel = ""
#print(FASTAFile)
for line in FASTAFile:
    if '>' in line:
        FASTLabel = line
        FASTDict[FASTLabel] = ""
    else:
        FASTDict[FASTLabel] += line
#print(FASTDict)
RESULTDist = {key: gc_content(value) for (key,value) in FASTDict.items()}
#print(RESULTDist)
MaxGCKey = max(RESULTDist, key=RESULTDist.get)
print(f'{MaxGCKey[1:]}\n{RESULTDist[MaxGCKey]}')

print(f'[7] + Aminoacids Sequence from DNA: {translate_seq(DNAStr,init_pos=0)}\n')

print(f'[8] + Codon Frequency: {codon_usage(DNAStr,"L")}\n')

print(f'[9] + Reading frames:')
for frame in gen_reading_frames(DNAStr):
    print(frame)

print(f'\n[10] + All proteins in 6 open reading frames')
for prot in all_proteins_from_orfs(DNAStr,0,0,True):
    print(f'{prot}')



