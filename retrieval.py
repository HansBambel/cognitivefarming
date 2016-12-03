#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 15:53:56 2016

@author: judith
"""

import numpy as np
#import string
import pandas


def retrieveSchutzmittel(culture=None, disease=None):
    # load database 
    database = pandas.read_pickle('database_python2.p')

    if(culture != None):
        
        # find all data connected to the selected culture
        data = database[database['Kultur'].str.contains(culture)]
                        
        # if no disease is given return all applicable products
        if(disease==None):
            # find all products that can be applied to selected culture
            product_list = list(set(data['Name'].tolist()))
            return product_list
            
        else:
            disease_data = database[database['Schadorganismus'].str.contains(disease)]
            products_to_disease = list(set(disease_data['Name'].tolist()))
            return products_to_disease

    # nothing given --> output all
    else:
        all_products = list(set(database['Name'].tolist()))
        return all_products


def retrieveBefall(culture=None):
    # load database
    database = pandas.read_pickle('database_python2.p')

    if (culture == None):
        product_list = list(set(database['Schadorganismus'].tolist()))
        flattened = [val for sublist in product_list for val in sublist]
        product_list = list(set(flattened))
        return product_list
        # find all data connected to the selected culture

    else:
        data = database[database['Kultur'].str.contains(culture)]
        # befall = list(set(data['Schadorganismus'].tolist()))
        befall = data['Schadorganismus'].apply(lambda x: x.split(', ')).tolist()
        flattened = [val for sublist in befall for val in sublist]
        befall = list(set(flattened))
        return befall


# input: culture (e.g. Kartoffel)
# culture = input("Welche Pflanzenkultur pflanzen Sie an? ")
# disease = input("Welchen Befall haben Ihre Pflanzen? ")

# product_list = retrieveSchutzmittel(culture, disease)
# product_list = retrieveBefall("Futterrübe")
# print(product_list)

#print(data)

#print('Sie können folgende Pflanzenschutzmittel benutzen: '+ data.Name)
