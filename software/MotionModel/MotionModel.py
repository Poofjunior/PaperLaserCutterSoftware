###############################################################################
# MotionModel.py
# Joshua Vasquez
# February 21, 2014
###############################################################################
import math


def lineToSteps(x1, y1, x2, y2, stepDist): 
    """ given two coordinates, pathToSteps returns the number of steps for 
    left and right motors to take to travel between those two coordinates. """ 
    # compute triangle base and height:
    deltaY = y2 - y1
    deltaX = x2 - x1

    # input to motion model:
    deltaA = (deltaX + deltaY)/math.sqrt(2)
    deltaB = (deltaX - deltaY)/math.sqrt(2)
    
    # convert total distance to steps:
    stepsA = deltaA/float(stepDist)
    stepsB = deltaB/float(stepDist)

    return [stepsA, stepsB]
    

## TODO: add up accumulated error and move to counteract it when it exceeds 
#        one step size.

## stepsTocmds does not handle accumulated error
def stepsToCmds(stepsA, stepsB):
    """given the number of steps to be traveled, stepsToCmds generates the 
    actual commands that drive the gantry"""
    # Handle divide-by-zero cases.
    if (stepsA == 0):
        for i in range(0,int(stepsB)):
            print "0 1"
        return
    if (stepsB == 0):
        for i in range(0,int(stepsA)):
            print "1 0"
        return;

    # Handle case where (max/min > 2).
    if (float(max(stepsA, stepsB))/float(min(stepsA,stepsB)) > 2):
        if (stepsA == max(stepsA, stepsB)):
            quotient = int(stepsA/stepsB)
            for i in range(0,int(stepsA)):
                if ((i % quotient == 0) and (stepsB > 0)):
                    # Both move.
                    print "1 1" 
                    stepsB = stepsB - 1
                else:
                    # Only A moves.
                    print "1 0"
        else:
            quotient = int(stepsB/stepsA)
            for i in range(0,int(stepsB)):
                if ((i % quotient == 0) and (stepsA > 0)):
                    # Both move.
                    print "1 1" 
                    stepsA = stepsA - 1
                else:
                    # Only B moves.
                    print "0 1"
        
        return

    # Handle case where (max/min < 2).
    else:
        if (stepsA == max(stepsA, stepsB)):
            quotient = int(stepsA/(stepsA -stepsB))
            for i in range(0,int(stepsA)):
                if (i % quotient == 0):
                    # Only A moves.
                    print "1 0" 
                else:
                    if (stepsB > 0):
                        # Both move.
                        print "1 1"
                        stepsB = stepsB - 1
                    else:
                        print "1 0"
        else:
            quotient = int(stepsB/(stepsA - stepsB))
            for i in range(0,int(stepsB)):
                if (i % quotient == 0):
                    # Only B moves.
                    print "0 1" 
                else:
                    if (stepsA > 0):
                        # Both move.
                        print "1 1"
                        stepsA = stepsA - 1
                    else:
                        print "0 1"
        
        return
    
    
 
