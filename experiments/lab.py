import argparse
import sys
import pickle
import os
from datetime import date

from warrant_test import test

def main():
    parser = argparse.ArgumentParser(description='Carry out an experiment.')
    choices = [ x for x in test.__dict__.keys() if len(x)>5 and x[:1].islower() and x!='pickle'] 
    parser.add_argument('experiment', metavar='EX', choices=choices, help='Experiment to be carried out')
    parser.add_argument('-p', '--percent', metavar='n%', type=float, default=10, help='Index value changed in percentage')
    parser.add_argument('-d', '--data', metavar='filename', default='twii', help='The data file to be processed (without extension)')
    parser.add_argument('-m', '--mode', metavar='mode', choices=('period', 'point'), default='point', help='The way to determine if a condition has been met')
    parser.add_argument('-s', '--start', metavar='startdate', default='1998-1-1', help='The start date')
    parser.add_argument('-e', '--end', metavar='enddate', default='2011-6-17', help='The end date')
    
    args = parser.parse_args()
    print args
    
    year, month, day = map(int, args.start.split('-'))
    startdate = date(year, month, day)
    year, month, day = map(int, args.end.split('-'))
    enddate = date(year, month, day)
    lab = test(startdate, enddate)
    
    
    
    path = os.path.abspath(os.path.join(os.path.dirname(__file__),'../data/'))
    data = pickle.load(open(os.path.join(path,args.data+".ser")))
    
    ratio = args.percent/100
    method = getattr(lab, args.experiment)
    method(data, ratio)
    
         
if __name__ == '__main__':
    main()