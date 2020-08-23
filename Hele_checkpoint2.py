# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 14:41:12 2020

@author: Kaja Amalie
"""
#%%1)

customers = ['James', 'John', 'Robert', 'Mary', 'Patricia', 'Jennifer']
salary = [155000, 755000,  455000, 1255000, 635000, 575000]
taxes = [55800, 317100, 182000, 451800, 171450, 71400]

def low_taxes(customers, salary, taxes):
    low_taxes = []
    for i in range(0, len(customers)):
        if taxes[i] / salary[i] < 0.3:
            low_taxes.append(customers[i])
    return(', '.join(low_taxes))




#%% 1) (med numpy or array)
customers = ["James", "John", "Robert", "Mary", "Patricia", "Jennifer"]
salary = [155000, 755000,  455000, 1255000, 635000, 575000]
taxes = [55800, 317100, 182000, 451800, 171450, 71400]

import numpy as np 

salary_np= np.array(salary)
print(salary_np)
taxes_np = np.array(taxes)
print(taxes_np)
tax_rate= list(taxes_np/salary_np)
print(tax_rate)

print(tax_rate)
for (x, y, z) in zip(customers, tax_rate, salary):
    if (y < 0.3) and (z > 500000):
        print(x, round(y,2), z)
        
#%%
        
def to_camel(text):
    new_text = ''
    text_list = text.split(' ')
    for word in text_list:
        new_text = new_text + word.capitalize()
    return(new_text)


def to_camel_case(text):
    camel_text = ''
    text_list = text.split(' ') # ['word1', 'word2', ...]
    for word in text_list: # word = 'word1'
        camel_text = camel_text + word[0].upper()+word[1:].lower()
    return(camel_text)
        



text = 'Hei på deg'
        
       
        

        
        
        
        
        
        
        
        
        
        
        
        