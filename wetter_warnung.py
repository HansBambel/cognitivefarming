#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 12:23:50 2016

@author: judith
""" 

import geoCodeWeather
import pandas

def wetter_check():
    # get weather forecast for the next week
    geoCodeWeather.wetterbericht('','Hasbergen')
    daten = pandas.read_csv('weatherData.csv')
    
    # check if temperature exceeds limit 
    check = daten[(daten['temp']<5) | (daten['temp']>25)]
    
    if(check.empty):
        return "Die Temperatur innerhalb der nächsten Woche liegt im empfohlenen Bereich."
    
    else:
        temperaturen = check['temp'].tolist()
        minimum = min(temperaturen)
        maximum = max(temperaturen)
        if(minimum<5):
            temp_info = str("Die Tiefsttemperatur innerhalb der nächsten Woche beträgt "+str(minimum)+"°C")
        elif(maximum>25):
            temp_info = str("Die Höchsttemperatur innerhalb der nächsten Woche beträgt "+str(maximum)+"°C")
        else:
            temp_info = ""
        warnung = "Warnung: Spritzeinsätze bei großer Hitze oder tiefen Temperaturen sind zu vermeiden. "
        return warnung+temp_info