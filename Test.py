# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 11:14:06 2020

@author: Abhilash
"""
#Sample test file to check Classic Stemmer->Porter Stemmer
import Classic_Stemmer.Classic_Stemmer as cs
#to use stem function,import the above library
if __name__=="__main__":
     str= "fundamentally"
     
     #the stem function takes a string arguement as input as -> def stem("abcd") and returns a string output
     st_output=cs.stem(str)
     print(st_output)
     
     str= "generalizations"
     
     print(cs.stem(str))
     str= "oscillator"
     
     print(cs.stem(str))
     str= "adjustible"
     
     print(cs.stem(str))

