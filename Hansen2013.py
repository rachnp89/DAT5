# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 10:43:12 2015

@author: rachael
"""
"""
Goal: determine which countries experienced greatest increase in tree cover loss
rates ( acceleration) between 2001-2013. 

Data: this analysis draws on the 30 meter annual Landsat-based product 
produced by Dr. Matt Hansen at the University of Maryland and Google. 
To download the original raster data, visit: 
http://data.globalforestwatch.org/datasets/93ecbfa0542c42fdaa8454fa42a6cc27

Data compiled in csv by Rachael Petersen by querying GFW data in Cartodb.com 

Relevant values in "UMD_30.csv" and "BRAZIL_TEST.csv"
'country' = country name
'year' = calendar year in which tree cover loss occured
'loss' = total tree cover loss in hectares that occurred in stated year
 'perc_change' = percent increase or decreases current year of tree cover loss represents as compared to previous year
 (note: 2001 is ommitted from data since it is the baseline year for loss, thus perc_change is null)

Analysis

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

# TEST USING BRAZIL 

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
results = est.fit()
results.summary()
results.rsquared
results.params    


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
deflist = world.values.tolist()

# reformatted data rows and columns to only include year and per_change
worldnew = pd.read_csv('/Users/rachael/Documents/DAT5-Project/data/country_change.csv')
worldlist = worldnew.values.tolist()

#create an empty list 
results = []

# iterate through countries and fill empty list with linregress results
for row in worldlist:
    country = row[0]    
    y = np.array([row[1:]]) # turn this into an array        
    x = np.array([2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013])
    slope, intercept, r_value, p_value, stderr = stats.linregress(x,y)
    add = [country, slope, intercept, r_value**2, p_value, stderr]
    results.append(add)

# write results of linregress for each country to a csv (incomplete)
import csv

with open("output1.csv", "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(results)

# complete same analysis, using annual % tree cover loss / extent(2000) as target variable
pnew = pd.read_csv('/Users/rachael/Documents/DAT5-Project/data/loss_perc_extnt.csv')
worldperc = pnew.values.tolist()

res = []
for row in worldperc:
    country = row[0]    
    y = np.array([row[1:]]) # turn this into an array        
    x = np.array([2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013])
    slope, intercept, r_value, p_value, stderr = stats.linregress(x,y)
    add = [country, slope, intercept, r_value**2, p_value, stderr]
    res.append(add)
    
import csv

with open("perc.csv", "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(res)
