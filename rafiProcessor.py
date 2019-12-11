import os
import sys
 
VERTEX_STRING = "vertex"
VERTEX_COUNT = 3
 
if len(sys.argv) > 0:
    # A or B
    FILE_KEY = sys.argv[1]
    MIN_X = float(sys.argv[2])
    MAX_X = float(sys.argv[3])
    MIN_Y = float(sys.argv[4])
    MAX_Y = float(sys.argv[5])
    # remove old processed file as we want to start fresh
    try:
        os.remove(FILE_KEY + "_processed.txt")
    except FileNotFoundError:
        print(FileNotFoundError)
         
     
    print("Opening file: " + FILE_KEY + ".txt")
    f= open(FILE_KEY + ".txt", "r")
    print("Adding new file: " + FILE_KEY + "_processed.txt")
    fp= open(FILE_KEY + "_processed.txt","w+")
 
    # check if both files where opened 
    if f.mode == 'r' and fp.mode == "w+":
        print("Succesfully opened data stream to both files")
         
        fl =f.readlines()
        print("Succesfully read lines of both files")
         
        # save previous line to skip duplicates
        prevLine= ""
         
        for line in fl:
         
            # does line contain vertex?
            if line.count(VERTEX_STRING) == 1:
                # extract the coordinates
                splitString = line.split(" ")[7:]
                joinedString = " ".join(splitString)
                x_value = float(splitString[0])
                y_value = float(splitString[1])
                IN_BOUNDS = x_value >= MIN_X and x_value <= MAX_X and y_value >= MIN_Y and y_value <= MAX_Y
 
                # skip duplicate lines
                if IN_BOUNDS and prevLine != joinedString:
                    prevLine = joinedString
                    fp.write(joinedString)   
                    print("wrote line", joinedString)
                else:
                    print("skipped line")
                     
        # Not sure if this works
        close(FILE_KEY + ".txt")
        close(FILE_KEY + "_processed.txt")
        print("done")
else: 
    print("Which file? enter A or B")
