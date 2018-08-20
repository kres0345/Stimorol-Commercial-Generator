#!/usr/bin/python3

#Used for splitting long text files into smaller files.

filename = "filename"
fileext = ".log"

Lines = open(filename+fileext,'r').readlines()

i = 0
while(i<len(Lines)):
    open(filename+str(i)+fileext,'w').write(Lines[i])
    print("Created file: "+filename+str(i)+fileext)
    i+=1
