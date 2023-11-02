import os

with open('input.tab', 'wt') as outf:
    for file in os.listdir("./04consensus_sequences/"):
        if file.endswith(".consensus.fasta"):
            outf.write(file.split('_')[0])
            outf.write('\t')
            outf.write(os.path.join("./04consensus_sequences/", file))
            outf.write('\n')
