# -*- coding: utf-8 -*-
"""
Created on Wed May 13 12:32:17 2020

@author: thinkpad
"""

# import necessary libraries
import pandas as pd
import xml.dom.minidom

# parse go_obo.xml into a DOM document object
DOMTree=xml.dom.minidom.parse('go_obo.xml')
# find root element
indexes=DOMTree.documentElement
# a list of 'terms' elements
terms=indexes.getElementsByTagName('term')
defs=[]
is_a=[]
dic={}

for term in terms:
    definitions=term.getElementsByTagName('def')
    IDs=term.getElementsByTagName('id')[0]
    is_as=term.getElementsByTagName('is_a')
    for x in is_as:
        is_a.append(x.childNodes[0].data)
    dic[IDs.childNodes[0].data]=is_a[:]
    is_a.clear()
    for definition in definitions:
        defstr=definition.getElementsByTagName('defstr')[0]
        defs.append(defstr.childNodes[0].data)    
a=[]
for x in range(len(defs)):
    if 'autophagosome' in defs[x]:
        a.append(x)
ids=[]
names=[]
d=[]
for i in a:
    IDs=terms.item(i).getElementsByTagName('id')[0]
    ids.append(IDs.childNodes[0].data)
    NAMEs=terms.item(i).getElementsByTagName('name')[0]
    names.append(NAMEs.childNodes[0].data)
    d.append(defs[i])
    
 # count the childnode 
childnode = []
for i in ids:
    m = []
    count = 0
    for j in dic:
        if i in dic[j]:
            count += 1
            m.append (j)
    n = m[:]
    inc = count
    while inc != 0 :
        m = []
        inc = 0
        for k in n:
            for j in dic:
                if k in dic[j]:
                    count += 1
                    inc += 1
                    m.append (j)
        n = m[:]
    childnode.append (count)
    
#output
xfile=pd.DataFrame({'id':ids,'name':names,'definition':d,'childnodes':childnode})
xfile.to_excel('Autophagosome.xlsx',
               sheet_name='Autophagosome',
               columns=['id','name','definition','childnodes'])
