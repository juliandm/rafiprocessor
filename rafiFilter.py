import os
import sys

if len(sys.argv) > 0:
    # A or B
    FILE_KEY = sys.argv[1]
    MIN_X = float(sys.argv[2])
    MAX_X = float(sys.argv[3])
    MIN_Y = float(sys.argv[4])
    MAX_Y = float(sys.argv[5])
    # remove old processed file as we want to start fresh
    try:
        os.remove(FILE_KEY + "_filtered.txt")
    except FileNotFoundError:
        print(FileNotFoundError)
         
     
    print("Opening file: " + FILE_KEY + "_processed.txt")
    f= open(FILE_KEY + "_processed.txt", "r")
    print("Adding new file: " + FILE_KEY + "_filtered.txt")
    fp= open(FILE_KEY + "_filtered.txt","w+")
 
    # check if both files where opened 
    if f.mode == 'r' and fp.mode == "w+":
        print("Succesfully opened data stream to both files")
         
        fl =f.readlines()
        print("Succesfully read lines of both files")

        for line in fl:
							
            # extract the coordinates
            splitString = line.split(" ")
            x_value = float(splitString[0])
            y_value = float(splitString[1])
            IN_BOUNDS = x_value >= MIN_X and x_value <= MAX_X and y_value >= MIN_Y and y_value <= MAX_Y

            # skip duplicate lines
            if IN_BOUNDS
                print("wrote line", line)
            else:
                print("skipped line")
                     
        # close
        f.close()
        fp.close()
        print("done")
else: 
    print("Which file? enter A or B. Which bounds?")
