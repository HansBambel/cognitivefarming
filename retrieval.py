#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 15:53:56 2016

@author: judith
"""

import numpy as np
#import string
import pandas


def retrieve(culture=None,disease=None):    
    # load database 
    database = pandas.read_pickle('database_python2.p')

    if(culture != None):
        
        # find all data connected to the selected culture
        data = database[database['Kultur'].str.contains(culture)]
                        
        # if no disease is given return all applicable products
        if(disease==None):
            # find all products that can be applied to selected culture
            product_list = data['Name'].tolist()
            return product_list
            
        else:
            disease_data = database[database['Schadorganismus'].str.contains(disease)]
            products_to_disease = disease_data['Name'].tolist()
            return products_to_disease
            
    else:
        all_products = database['Name'].tolist()
        return all_products
            
            
# input: culture (e.g. Kartoffel)
culture = input("Welche Pflanzenkultur pflanzen Sie an? ")
disease = input("Welchen Befall haben Ihre Pflanzen? ")

product_list = retrieve(culture,disease)
print(product_list)

    
                
    


#print(data)

#print('Sie können folgende Pflanzenschutzmittel benutzen: '+ data.Name)
