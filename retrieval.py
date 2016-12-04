#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 15:53:56 2016

@author: judith
"""
#import string
import pandas


def retrieveSchutzmittel(culture="", disease=""):
    # load database 
    database = pandas.read_pickle('database.p')

    if (culture != ""):
        
        # find all data connected to the selected culture
        data = database[database['Kultur'].str.contains(culture)]
        # if no disease is given return all applicable products
        if disease == "":
            # find all products that can be applied to selected culture
            product_list = list(set(data['Name'].tolist()))
            return product_list
            
        else:
            disease_data = data[data['Schadorganismus'].str.contains(disease)]
            products_to_disease = list(set(disease_data['Name'].tolist()))
            return products_to_disease

    # nothing given --> output all
    else:
        all_products = list(set(database['Name'].tolist()))
        return all_products


def retrieveBefall(culture=""):
    # load database
    database = pandas.read_pickle('database.p')

    if (culture == ""):
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

def retrieveCultures():
    # load database
    database = pandas.read_pickle('database.p')
    product_list = database['Kultur'].apply(lambda x: x.split(', ')).tolist()
    flattened = [val for sublist in product_list for val in sublist]
    product_list = list(set(flattened))
    return product_list
    
def retrieveProductInfo(product,culture,befall):
    # load database
    database = pandas.read_pickle('database.p')
    
    # find information to product
    data = database[database['Name'].str.contains(product)]
    
    if(culture != ""):
        data = data[data['Kultur'].str.contains(culture)]
    
    if(befall != ""):
        data = data[data['Schadorganismus'].str.contains(befall)]
    
    # extract information
    wirkstoff = list(set(data['Wirkstoff'].tolist()))
    wirkstoffgehalt = list(set(data['Wirkstoffgehalt'].tolist()))
    zulassungsende = list(set(data['Zulassungsende'].tolist()))
    
    anwenderschutz = list(set(data['Anwenderschutz'].tolist()))
    gewässerschutz = list(set(data['Gewässerschutz'].tolist()))
    bienenschutz = list(set(data['Bienenschutz'].tolist()))
    nutzorganismen = list(set(data['Nutzorganismen'].tolist()))
    sonstiges = list(set(data['Sonstiges'].tolist()))
    gefahrenstoffverordnung = {'Anwenderschutz': anwenderschutz, 'Gewässerschutz': gewässerschutz, 'Bienenschutz': bienenschutz, 'Nutzorganismen': nutzorganismen, 'Sonstiges': sonstiges}
    
    hinweise = list(set(data['Anwendungshinweise'].tolist()))
    
    return wirkstoff,wirkstoffgehalt,zulassungsende,gefahrenstoffverordnung,hinweise

    

# input: culture (e.g. Kartoffel)
# culture = input("Welche Pflanzenkultur pflanzen Sie an? ")
# disease = input("Welchen Befall haben Ihre Pflanzen? ")

# product_list = retrieveSchutzmittel(culture, disease)

# product_list = retrieveBefall("Futterrübe")
# print(product_list)

# print(retrieveCultures())

#print(data)

#print('Sie können folgende Pflanzenschutzmittel benutzen: '+ data.Name)


