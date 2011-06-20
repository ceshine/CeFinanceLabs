import pickle
import sys
import os
from datetime import date

class test(object):
    TRADE_DAYS = 50
    def __init__(self, startdate, enddate):
        self.FROM = startdate
        self.TO = enddate
    
    
    def slice_by_time(self, data):
        start, end = -1, 0
        for idx, entry in enumerate(data):
            if start == -1 and entry[0] >= self.FROM:
                start = idx
                end = -1
            if end == -1 and entry[0] > self.TO:
                end = idx
                break
        
        if end == -1:
            end = len(data)
        
        return data[start:end]
        
    def summarize(self, hit):
        count = 0
        for item in hit:
            if item == 'x':
                count += 1
        return count, float(count)/len(hit)
    
    def percent(self, data, ratio, mode='period'):
        data = self.slice_by_time(data)
        
        hit = []       
        for i in range(0, len(data)-self.TRADE_DAYS):
            buyat = data[i][1]
            flag = 'o'
            if mode=='period':
                for j in range(i+1, i+self.TRADE_DAYS):
                    if (data[j][1]-buyat)/buyat * ratio >= ratio * ratio:
                        flag = 'x'
                        break
                hit.append(flag)
            elif mode=='point':
                if (data[i+self.TRADE_DAYS][1]-buyat)/buyat <= -0.1:
                    hit.append('x')
                else:
                    hit.append('o')
           
            
        print "".join(hit)
        count, prob = self.summarize(hit)
        print len(hit), count, prob
            