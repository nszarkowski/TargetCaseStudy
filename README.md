# TargetCaseStudy
Case Study for Target Software Engineer Position - System Programming
Created by - Nicholas Boder-Szarkowski

Most Current Version to Run - Version 3

Before Running:
Start with installing Python.
Current Version is here https://www.python.org/downloads/
If Python is already installed make sure it is version 3.8+.
Now open a Command prompt with proper privalage to write a json file.

From Command Prompt:
change cd (Current Directory) to where the program is on your machine.
Run the program by running the python File_Name.py

Execution:
You will be asked to enter a mount point.
Enter said point either a drive or file location.
The script will give you an output of all files in location and how many bytes of data they are using.

For testing:
When running in a test enviornment 3 assumptions were made.
1. You are able to have propper privilage to write to json file if you don't the first version of the program still gives out the data just not in json format.
2. Your desired mount point is accessable since the system does check if you enter a mount point but, doesn't make the mount point for you.
3. You only want file information and not folder information since a folder could be using more data however when getting folder data with V1-V2 you only return a 0 value.


