#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 15:47:42 2021

@author: nielchonoolal
"""

#finding max in a unsorted list 

def find_max(lst):
    #base case to terminate recursive function 
    if len(lst) == 1:
        return lst[0]
    else:
        #if first element is greater than the second
        if lst[0] < lst[1]:
            return find_max(lst[1:])
        else:
            #if second element is greater than the first
            new = lst[1:]
            new.append(lst[0])
            return find_max(new)
        
        
        
my_list = [1,3,100,2,1,12,90]
print(find_max(my_list))