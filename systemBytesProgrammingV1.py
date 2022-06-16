#Nicholas Boder-Szarkowski
#System Programming Python script for Target Case Study Interview

#import os, Json, and shutil
#os to run through file hierarchy
#Json to format and show output in Json format
#shutil to calculate the byte information
import os
import json
import shutil

#Declare variable to manipulate and dictionary for result display
path = input('Enter Mount Point File Path')
result = {}

#using os.path.ismount method to make sure the file path you input is mounted
#if statement to error correct if you have the wrong file path
ismount = os.path.ismount(path)
if ismount == True:
    #using os.listdir method to find all sub directories for mount point only one level down
    subDirectoryList = os.listdir(path)
    #using while loop create a list array with pairings of the original path root and the subdirectory files list
    i = 0
    while i < len(subDirectoryList):
        # check if the sub directory is a file
        for j in subDirectoryList:
            if os.path.isfile(j):
                toCount = (path+"/"+subDirectoryList[i])
                size = os.path.getsize(toCount)
                result[toCount] = size
                i+=1
            else:
                i+=1
    print(result)
    
else:
    print(path, 'is not a mounted directory')