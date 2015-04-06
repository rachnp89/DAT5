# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 11:17:42 2015

@author: rachael
"""


import pandas as pd
import matplotlib.pyplot as plt

# loads the data
auto = pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT5/master/data/auto_mpg.txt', sep="|")

# Part 1
auto.groupby('cylinders').mpg.mean().plot(kind='bar', title='average mpg by no. of cylinder')

"""
Produces a bar graph showing mean mpg for 3, 4, 5,6, and 8 cylinders
The data is slightly skewed to the left; the max mean mpg occurs at 4 cylinders
and decreases as mpg increases, with the minimum mean mpg occuring at 8 cylinders
Strictly considering cylinders and mpg, it seems the optimal no. of cylinders is 4
""" 

# Part 2
pd.scatter_matrix(auto)
plt.show()
"""
Creates a scatter matrix that plots mpg, cylinders, displacement, horsepower,
weight, acceleration, model_+year and origin against eachother. 
Horsepower, weight, and displacement are all positively correlated -- e.g.
the more a car weighs, the higher its displacement, and vise-versa. 
These three variables also have the clearest inverse correlation with mpg. 
For example, the greater the displacement, horsepower or weight, the lower the mpg.
"""
# Part 3
# Creates a scatter plot with weight as x and mpg as y 
auto.plot(kind='scatter', x='weight', y='mpg', alpha=0.4)
plt.show()
# As weight (x) increases, mpg (y) decreases. Lighter cars get better mpg. 


# Creates a scatterplot using horsepower as the x and displacement as the y
auto.plot(kind='scatter', x='displacement', y='horsepower', alpha=0.4)
plt.show()
'''
Displacement and horsepower are positively correlated so that generally, the
higher the horsepower, the higher the displacement. However, 
there is a notable variability of horsepower at displacement = 100 and
displacement = 350.
'''

# Creates histogram of acceleration values
auto.acceleration.hist()
plt.title("Distribution of Acceleration")
plt.xlabel('Acceleration')
plt.ylabel('Frequency')
plt.show()
'''
Acceleration is evenly distributed, with the fewest occurrences at the min
(8) and maximum (26) and the most occurences (n=90) occuring at 16.
'''
# creates a histogram for mpg for each cylinder group (3,4,5,6,8)
auto.groupby('cylinders').mpg.hist()
plt.title("Distribution of mpg")
plt.xlabel('mpg')
plt.ylabel('Frequency')
plt.legend(x='3,4,5,6,8',loc='upper right')
plt.show()

auto.groupby('cylinders').value_counts


# do cars made before or after 1975 get better average mpg? (Hint: You need to 
#create a new column that encodes whether a year is before or after 1975.)

if auto[auto.model_year > 75]:
    auto['after_75'] = True
else: 
    auto['after_75'] = False
    
# create a new column with 0 for cars before 75 and 1 for cars created after 75
auto['after_75'] = (auto['model_year'] < 75).astype(int)
auto['after_75'] = (auto['model_year'] > 75).astype(int)

auto[auto.after_75 == 0].mpg.mean()
auto[auto.after_75 == 1].mpg.mean()

'''
cars before 75 got an average of 19.394444 mpg, while cars produced after 75
got better mpg, around 26.8858 mpg.
'''