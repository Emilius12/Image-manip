# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 21:33:48 2023

@author: emile
"""

import numpy as np
from copy import deepcopy
from PIL import Image

# Chargement de l'image
image_path = r"C:\Users\emile\Desktop\Image manipulation\gloaming.jpg"
image = Image.open(image_path)

array = np.array(image)


def moyenne(array,x,y):
    s = 0 
    for i in range (3):
        s+= int(array[x][y][i]/3)
    res = [s,s,s]
    return res



def flou(array,x,y):
    res = [0,0,0]
    if x == 0 or y  == 0 or x == len(array)-1 or y == len(array[0])-1:
        return array[x,y]
    for i in range (3):
        if (array[x+1,y][i])/3+(array[x-1,y][i])/3+(array[x,y+1][i])/3+(array[x,y-1][i])/3 == None :
            res[i] =  array[x,y][i]
    
        else: 
            res[i] = int((array[x+1,y][i])/3+(array[x-1,y][i])/3+(array[x,y+1][i])/3+(array[x,y-1][i])/3)
    return res

def apply (f,array):
    new = np.copy(array)
    for x in range (len(array)):
        for y in range (len(array[0])):
            new[x][y] = f(array,x,y)
    return Image.fromarray( new )      
            
            



























