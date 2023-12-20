#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 19:08:20 2023

@author: hamish
"""

#%%
#To plant filter all files in the folder
#Firt install plant using conda install -c plant plant

cd /path/to/folder/with/files

# Loop through all the .tif files in the directory
for file in *.tif; do
    plant_filter.py "$file" -a 3 -r 3 -o "${file%.tif}_filter.tif" --of GTiff
done




#%%