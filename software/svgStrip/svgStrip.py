#!/usr/bin/python

# svgStrip.py
# Author: Joshua Vasquez
# Date: February 15, 2014
import sys

units = ""
unitsFound = False
unitList = ['"pt"', '"pc"', '"mm"', '"cm"', '"in"']
# conversion factor to steps: 
#TODO: actually put in the right conversion factor to steps:
convFactor = [1, 1, 1, 1, 1]

###############################################################################
###############################################################################
def findUnits(lineIn): 
    global unitList 

    for unit in unitList:
        #index = lineIn.find(unit) 
        index = lineIn.find(unit) 
        if index != -1:
            #print unit
            return unit
    return ""


###############################################################################
###############################################################################
def convertToSteps():
    global units, unitList, convFactor

    for i in range(0,len(unitList)):
        if (unitList[i] == units):
            # TODO: actually convert the entire file
            return convFactor[i]  
    return


###############################################################################
###############################################################################
if len(sys.argv) < 2:
    sys.exit(0)
else:
    print "opening " + sys.argv[1]
    inFile = open(sys.argv[1])
    outFile = open('output.txt', 'w')

    # while not the end of the file:
    for line in inFile:
        # parse for path data:
        line = line.strip()
        
        if (unitsFound == False): 
            units = findUnits(line) 
            if (units in unitList):
                unitsFound = True

        if (line != ""):
#            print line[0]
            if (line[0:2] == 'd='):
                line = line.strip("d=")
                line = line.strip('"')
                outFile.write(line)
                outFile.write('\n')

    print convertToSteps()
       



