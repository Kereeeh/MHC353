#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 18:50:07 2017

@author: Keri
"""
import folium 
import csv

#encoding takes care of the utf-8 codec error
f = open("0301_comp.csv",encoding="latin-1")
reader = csv.DictReader(f)

map = folium.Map(location=[40.7384951,-73.8849147], zoom_start=15)

for row in reader: 
    lat = row["Latitude"]
    long = row["Longitude"]
    comp = row["Complaint Type"]
    if not lat and not long:
        print("Keri is the Best")
    else:
        if comp == "Blocked Driveway":
            map.simple_marker([lat,long],popup=comp, marker_color='red')
        else:
            map.simple_marker([lat,long],popup=comp, marker_color='blue')

map.create_map(path='0301_hw.html')


    
