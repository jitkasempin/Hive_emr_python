#!/usr/bin/env python
# encoding: utf-8

import sys, os, re
from math import log, sqrt
import simplejson
import statsmodels

(t,e) = (0,0)
iterate_row = 0
sumOfX = 0
sumOfY = 0
sumOfXSq = 0
sumOfYSq = 0
ssX = 0
ssY = 0
sumCodeXY = 0
timeDayCount = 0
sCo = 0

for line in sys.stdin:
    gaDate, gaVisits, gaBounces = line.strip().split("\t")
    # dates = simplejson.loads(dates)
    # pageviews = simplejson.loads(pageviews)
    if iterate_row == 0:
        visit_list = []
        XI = []
        acc_visits = 0
    else:
        try:
            visitors = int(gaVisits)
            visit_list.append(visitors)
            XI.append(timeDayCount)
            #summation = sum(visit_list)
            #sumCodeXY += visitors * timeDayCount
            #sumOfX += visitors
            #sumOfY += timeDayCount
            #sumOfXSq += visitors * visitors
            #sumOfYSq += timeDayCount * timeDayCount
            timeDayCount += 1
            #daily_trend, error = calc_daily_trend(gaDate, visitors, visit_list, summation)
        except:
            # skip bad rows
            daily_trend = 0
            error = 0
        #(t,e) = (daily_trend,error)
        #sys.stdout.write('%s\t%s\t%s\n' % (gaDate, daily_trend, error))
    if iterate_row == 180:
        slope, intercept, r_value, p_value, std_err = stats.linregress(XI,visit_list)
        (t,e) = (slope,intercept)
        sys.stdout.write('%s\t%s\n' % (slope,intercept))

    iterate_row += 1

#ssX = sumOfXSq - ((sumOfX * sumOfX) / iterate_row)
#ssY = sumOfYSq - ((sumOfY * sumOfY) / iterate_row)
#RNumerator = (iterate_row * sumCodeXY) - (sumOfX * sumOfY)
#RDenom = (iterate_row * sumOfXSq - (sumOfX * sumOfX)) * (iterate_row * sumOfYSq - (sumOfY * sumOfY))
#sCo = sumCodeXY - ((sumOfX * sumOfY) / iterate_row)
#meanX = sumOfX / iterate_row
#meanY = sumOfY / iterate_row
#dblR = RNumerator / sqrt(RDenom)
#rsquared = dblR * dblR
#yintercept = meanY - ((sCo / ssX) * meanX)
#slope = sCo / ssX


