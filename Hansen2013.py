# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 10:43:12 2015

@author: rachael
"""
"""
Goal: determine which countries experienced the greatest acceleration in
deforestation between 2001-2013. 

Data: this analysis draws on the 30 meter annual Landsat-based product 
produced by Dr. Matt Hansen at the University of Maryland and Google. 
To download the raw data, visit: http://earthenginepartners.appspot.com/science-2013-global-forest
or www.globalforestwatch.org
Data compiled in csv by Rachael Petersen by querying Cartodb. 

Relevant values in "UMD_30.csv" and "BRAZIL_TEST.csv"
'country' = country name
'year' = calendar year in which tree cover loss occured
'loss' = total tree cover loss in hectares that occurred in stated year
 'perc_change' = percent increase or decreases current year of tree cover loss represents as compared to previous year
 (note: 2001 is ommitted from data since it is the baseline year for loss, thus perc_change is null)

Analysis steps:

For each country: 

1) Fit a least squares regression line, using 
"year" as the predictor variable (2002-2013)
and "perc_change" as the explanatory (target) variable.

2) Write results to a csv, with one row for each country, and one column for
each of the following: "country", gradient, R2, P-value and intercept. 

3) Compare gradient values for statistically significant regressions. Highest values
indicate countries with greatest acceleration -- lowest values indicate countries with
decelerating rates of change. 
""" 


# toying with statsmodels
import numpy as np
import pandas as pd
import statsmodels.api as sm

# import data array with annual deforestation data for Brazil
defor = pd.read_csv('/Users/rachael/Documents/DAT5-Project/data/BRAZIL_TEST.csv')  

# remove 2001 
brazil = defor.drop(defor.index[[0]])

# predictor variable is year, explanatory variable is the percent change in deforestation from year to year
X = brazil.year
y = brazil.perc_change
X = sm.add_constant(X)
X.head()

est = sm.OLS(y, X)
est = est.fit()
est.summary()


# now, with scipy!
import numpy as np
import pandas as pd
from scipy import stats
x = brazil.year
y = brazil.perc_change
gradient, intercept, r_value, p_value, slope_std_error = stats.linregress(x,y)
print "r-squared:", r_value**2
print gradient
print intercept

# open file of annual deforestation data for the whole world 
world = pd.read_csv('/Users/rachael/Documents/DAT5-Project/data/UMD_30.csv') 
world.groupby('country').count() 




# write results to a csv (incomplete)
import csv

c = csv.writer(open("output.csv", "wb"))
c.writerow(["country","gradient","r_value","p_value","slope_std_error","intercept"])

res = [brazil.country, gradient, (r_value**2), p_value, slope_std_error, intercept]

writer.writerows(res)


