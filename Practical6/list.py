# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 09:45:47 2020

@author: thinkpad
"""
gene_lengths = [0 for i in range(10)]
# input gene_lengths
for i in range(0,10):
    gene_lengths[i] = int(input())
min = 0
max = 0
# for i = 0 to 10
# max = the subscript of max(gene_lengths[0:10])
# min = the subscript of min(gene_lengths[0:10])
for i in range (1,10):
    if gene_lengths[min] > gene_lengths[i]:
        min = i
    if gene_lengths[max] < gene_lengths[i]:
        max = i
# Remove the latter one first. 
if min>max:
    gene_lengths.remove(gene_lengths[min])
    gene_lengths.remove(gene_lengths[max])
else:
    gene_lengths.remove(gene_lengths[max])
    gene_lengths.remove(gene_lengths[min])
print (gene_lengths)


import matplotlib.pyplot as plt
plt.boxplot(gene_lengths,vert=True,whis=1.5,
            patch_artist=True,meanline=True,showbox=True,
            showcaps=True,showfliers=True,notch=False)
plt.show()
