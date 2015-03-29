# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 17:38:02 2015

@author: rachael
"""

# PART 1
import pandas as pd
auto = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT5/master/data/auto_mpg.txt', sep="|")

# PART 2
auto.shape
# There are 392 rows and 9 columns
auto.columns
# Variables are mpg, cylinders, displacement, horsepower, weight, acceleration
# model_year, origin and car_name
auto.describe()
# minimum mpg is 9, maximum is 46.6
# minimum cylinders is 3, maximum is 8
# minimum displacement is 68, maximum is 455
# minimum horsepower is 46, maximum is 230
# minimum weight is 1613, maximum is 5140
# minimum acceleration is 8, maximum is 24.8
# earliest model year is (19)70, latest is 1982
# minimum origin is 1, maximum is 3

# avg mpg == 23.45, med == 22.75, slightly skewed left.
# greater number of vehicles 

# avg cylinder == 5.4719, med == 4.0

# avg displacement == 194.411, med == 151

# avg horsepower == 104.47, med == 95.5
# skewed left, meaning more observations with lower horespower

# avg weight == 2977.584, med == 2803.5

# avg acceleration == 15.541, med == 15.5, 
# even distribution of acceleration across data set

# avg model_year == 75.98, med == 76
# even distribution of years across data set 

# avg origin == 1.576, med == 1.0

# PART 3
auto.sort_index(by='mpg', ascending=False).head(5)   
# mazda glc, honda civic 1500 gl, vw rabbit c (diesel), vw pickup, vw dasher (diesel)
# are the 5 cars that get the best gas mileage

auto[auto.cylinders > 4].sort_index(by='mpg', ascending=False).head(5)
# oldsmobile cutlass ciera (diesel), audi 5000s (diesel), datsun 280-zx, volvo diesel, and chevrolet citation
# are the most gas efficint cars with more than 4 cylinders.

auto.sort_index(by='mpg', ascending=True).head(5)      
# the hi 1200d, chevy c20, ford f250, dodge d200, and oldsmobile omega get the worst gas mileage.

auto[auto.cylinders <= 4].sort_index(by='mpg', ascending=True).head(5)
# maxda rx3, volvo 145e (sw), volvo 144ea, mazda rx2 coupe, and ford pinto
# are the five cars with 4 or fewer cylinders that get the worst gas mileage

# PART 4
# which variable have the greatest effect on mpg? 
