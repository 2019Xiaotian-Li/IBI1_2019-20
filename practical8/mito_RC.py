# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 12:58:28 2020

@author: thinkpad
"""
reseq = []
Name = []
gene = []
s=''
count = 0
s1 = ''
xfile = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
for line in xfile:
    if line.startswith ('>'):
        if s!='':
            gene.append(s)
        s = line[1:8]
        Name.append(s)
        count = count + 1
        s = ''
    else:
        s = s + line 
gene.append(s)

for j in range(count):
    seq = gene[j]
    s1 = ''
    for i in range(len(seq)):    
        if seq[i] == 'A':
            s1 = 'T' + s1
        elif seq[i] == 'C':
            s1 = 'G' + s1
        elif seq[i] == 'G':
            s1 = 'C' + s1
        elif seq[i] == 'T':
            s1 = 'A' + s1
    reseq.append(s1)

n = input ('please input the file name')
fout = open(n,'w')
for i in range(count):
    line1 = Name[i] + '   ' + str(len(gene[i])) + '\n'
    line2 = reseq[i] + '\n'
    fout.write(line1)
    fout.write(line2)

try:
	xfile = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa', 'r')
finally:
	if xfile:
		xfile.close()
fout.close()

  