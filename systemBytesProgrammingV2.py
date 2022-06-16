#Nicholas Boder-Szarkowski
#System Programming Python script for Target Case Study Interview

#import os, Json, and shutil
#os to run through file hierarchy
#Json to format and show output in Json format
#pathlib to change file path into propper format depending on Operating System
import os
import json
from pathlib import Path

#Declare variable to manipulate and dictionary for result display
path = input('Enter Mount Point: ')
#pathSave variable to use pathlib function when searching the directory with propper slash work
pathSave = Path(path)
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
                #pathData is just to be text on return result whereas toCount is actual system path with proper slash work to account for different operating systems
                #pathData is needed since Json won't work with operating system type as an entery for indexing
                pathData = (path+"/"+subDirectoryList[i])
                toCount = pathSave / subDirectoryList[i]
                size = os.path.getsize(toCount)
                result[pathData] = size
                i+=1
            else:
                i+=1
        #creating Json File to dump dictionary data into a Json File
    resultFormated = json.dumps(result, indent = len(result))
    with open("data.json", "w") as outfile:
        outfile.write(resultFormated)
    print(result)
        
else:
    print(path, 'is not a mounted directory')