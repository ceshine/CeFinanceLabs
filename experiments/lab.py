import argparse
import sys

import warrant_test

def main():
    parser = argparse.ArgumentParser(description='Carry out a experiment.')
    choices = [ x for x in warrant_test.__dict__.keys() if len(x)>5 and x[:1].islower() and x!='pickle'] 
    parser.add_argument('experiment', metavar='EX', choices=choices, help='Experiment to be carried out')

    args = parser.parse_args()
    print args.experiment
    warrant_test.__dict__[args.experiment]()
        
         
if __name__ == '__main__':
    main()