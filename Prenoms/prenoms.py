# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 19:23:49 2024

@author: Samuel
"""

def isValid(name):
    if name[0] == 'S':
        return False
    if name[0] == 'A':
        return False
    if 'R' in name:
        return False
    if '-' in name:
        return False
    if 'R' in name:
        return False
    if 'R' in name:
        return False
    return True

def analyse(filename, N = 500):
    
    L = []
    current = 'NOT_A_NAME'
    
    with open(filename, encoding='utf-8') as file:
        firstLine = True
        for line in file:
            if firstLine:
                firstLine = False
            else:
                data = line.split(';')
                
                name = data[1]
                count = int(data[3])
                
                if name == '_PRENOMS_RARES':
                    continue
                
                if name == current:
                    L[-1][1] += count
                else:
                    L.append([name, count])
                    current = name
    
    L.sort(key = lambda x:x[1])
    for item in L[:5]:
        print(item[0], ":", item[1])
    print("...")
    for item in L[-5:]:
        print(item[0], ":", item[1])
    print("Just ordered", len(L), "names.")
    
    AcceptedNames = []
    for item in L[-N:]:
        if isValid(item[0]):
            AcceptedNames.append(item)
    
    print("Accepted", len(AcceptedNames), "names out of", N, "most common.")
    """
    for item in AcceptedNames:
        print(item[0], ":", item[1])
    """
    print([item[0] for item in AcceptedNames])
    
    
print("Prénoms données aux enfants assignés femmes")
analyse("F.csv")
print("")
print("Prénoms données aux enfants assignés hommes")
analyse("M.csv")
