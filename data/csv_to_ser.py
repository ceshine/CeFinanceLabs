import sys
import csv
import datetime
import pickle

def main():
    if len(sys.argv) != 3:
        print "Usage: csv_to_ser [original.csv] [target.ser]"
    original = sys.argv[1]
    target = sys.argv[2]
    
    reader = csv.reader(open(original, 'rb'), delimiter=',')
    
    fieldnames = reader.next()
    
    result = []
    #result.append((fieldnames[0], fieldnames[-1], fieldnames[-2]))
    for row in reader:
        year, month, day = map(int, row[0].split('-'))
        date = datetime.date(year, month, day)
        point = float(row[-1])
        volume = int(row[-2])
         
        result.append((date, point, volume))
    
    result.sort(key=(lambda x: (x[0]).toordinal()))
    #print result[:5]

    pickle.dump(result, open(target,'wb'))
             
    
if __name__ == '__main__':
    main()
