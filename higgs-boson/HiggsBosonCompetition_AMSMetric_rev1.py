# -*- coding: utf-8 -*-
"""
Evaluation metric for the Higgs Boson Kaggle Competition,
as described on:
https://www.kaggle.com/c/higgs-boson/details/evaluation

@author: Joyce Noah-Vanhoukce
Created: Thu Apr 24 2014
"""

import os
import csv
import math


def create_solution_dictionary(solution):
    """ Read solution file, return a dictionary with key EventId and value (weight,label).
    Solution file headers: EventId, Label, Weight """
    
    solnDict = {}
    with open(solution, 'rb') as f:
        soln = csv.reader(f)
        soln.next() # header
        for row in soln:
            if row[0] not in solnDict:
                solnDict[row[0]] = (row[1], row[2])
    return solnDict

        
def check_submission(submission, Nelements):
    """ Check that submission RankOrder column is correct:
        1. All numbers are in [1,NTestSet]
        2. All numbers are unqiue
    """
    rankOrderSet = set()    
    with open(submission, 'rb') as f:
        sub = csv.reader(f)
        sub.next() # header
        for row in sub:
            rankOrderSet.add(row[1])
            
    if len(rankOrderSet) != Nelements:
        print 'RankOrder column must contain unique values'
        exit()
    elif rankOrderSet.isdisjoint(set(xrange(1,Nelements+1))) == False:
        print 'RankOrder column must contain all numbers from [1..NTestSset]'
        exit()
    else:
        return True

    
def AMS(s, b):
    """ Approximate Median Significance defined as:
        AMS = sqrt(
                2 { (s + b + b_r) log[1 + (s/(b+b_r))] - s}
              )        
    where b_r = 10, b = background, s = signal, log is natural logarithm """
    
    br = 10.0
    radicand = 2 *( (s+b+br) * math.log (1.0 + s/(b+br)) -s)
    if radicand < 0:
        print 'radicand is negative. Exiting'
        exit()
    else:
        return math.sqrt(radicand)


def AMS_metric(solution, submission):
    """  Prints the AMS metric value to screen.
    Solution File header: EventId, Class, Weight
    Submission File header: EventId, RankOrder, Class
    """
    
    numEvents = 550000 # number of events = size of test set
    
    # solutionDict: key=eventId, value=(label, class)
    solutionDict = create_solution_dictionary(solution)

    signal = 0.0
    background = 0.0
    if check_submission(submission, numEvents):
        with open(submission, 'rb') as f:
            sub = csv.reader(f)
            sub.next() # header row
            for row in sub:
                if row[2] == 's': # only events predicted to be signal are scored
                    if solutionDict[row[0]][0] == 's':
                        signal += float(solutionDict[row[0]][1])
                    elif solutionDict[row[0]][0] == 'b':
                        background += float(solutionDict[row[0]][1])
     
        print 'signal = {0}, background = {1}'.format(signal, background)
        print 'AMS = ' + str(AMS(signal, background))


if __name__ == "__main__":

    # enter path and file names here    
    path = ""
    solutionFile = ""
    submissionFile = ""
    
    AMS_metric(solutionFile, submissionFile)
    
    
