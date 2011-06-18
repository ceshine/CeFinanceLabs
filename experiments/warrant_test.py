import pickle
import sys
import os
from datetime import date

TRADE_DAYS = 50
FROM = date(1998, 1, 1)
TO = date(2011, 6, 19)  

def slice_by_time(data):
    start, end = -1, 0
    for idx, entry in enumerate(data):
        if start == -1 and entry[0] >= FROM:
            start = idx
            end = -1
        if end == -1 and entry[0] > TO:
            end = idx
            break
    
    if end == -1:
        end = len(data)
    
    return data[start:end]
    
def summarize(hit):
    count = 0
    for item in hit:
        if item == 'x':
            count += 1
    return count, float(count)/len(hit)

def up10percent_atend(data):
    data = slice_by_time(data)
    
    hit = []       
    for i in range(0, len(data)-TRADE_DAYS):
        buyat = data[i][1]
        if (data[i+TRADE_DAYS][1]-buyat)/buyat >= 0.1:
            hit.append('x')
        else:
            hit.append('o') 
        
    print "".join(hit)
    count, prob = summarize(hit)
    print len(hit), count, prob

def up10percent(data):
    data = slice_by_time(data)
    
    hit = []       
    for i in range(0, len(data)-TRADE_DAYS):
        buyat = data[i][1]
        flag = 'o'
        for j in range(i+1, i+TRADE_DAYS):
            if (data[j][1]-buyat)/buyat >= 0.1:
                flag = 'x'
                break
        
        hit.append(flag)
        
    print "".join(hit)
    count, prob = summarize(hit)
    print len(hit), count, prob
         
def noless_atend(data):
    data = slice_by_time(data)
    
    hit = []     
    for i in range(0, len(data)-TRADE_DAYS):
        buyat = data[i][1]
        if data[i+TRADE_DAYS][1] >= buyat:
            hit.append('x')
        else:
            hit.append('o')
        
    print "".join(hit)
    count, prob = summarize(hit)
    print len(hit), count, prob
    
def down10percent_atend(data):
    data = slice_by_time(data)
    
    hit = []     
    for i in range(0, len(data)-TRADE_DAYS):
        buyat = data[i][1]
        if (data[i+TRADE_DAYS][1]-buyat)/buyat <= -0.1:
            hit.append('x')
        else:
            hit.append('o')
        
    print "".join(hit)
    count, prob = summarize(hit)
    print len(hit), count, prob
    
def main():
    if len(sys.argv) != 3:
        print "Usage: warrant_test [serfile] [experiment_to_be_tested]"
    
    path = os.path.abspath(os.path.join(os.path.dirname(__file__),'../data/'+sys.argv[1]))
    data = pickle.load(open(path))
    
    options = { 'up10percent': up10percent_atend,
                'noless': noless_atend,
                'down10percent': down10percent_atend }
    
    options[sys.argv[2]](data)
    
         
if __name__ == '__main__':
    main()