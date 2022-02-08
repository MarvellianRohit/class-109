from pickle import FALSE
import random
from numpy import append
import plotly.figure_factory as ff
import statistics

result = []
for i in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    result.append(dice1+dice2)

mean = statistics.mean(result)
print("mean =",mean)
median = statistics.median(result)
print("median =",median)
mode = statistics.mode(result)
print ("mode = ", mode)
std = statistics.stdev(result)
print("Standard Deviation =",std)


gr = ff.create_distplot([result],["Result"],show_hist=False)
gr.show()

first_std_start  = mean - std
first_std_end = mean + std

second_std_start = mean - (std*2)
second_std_end = mean + (std*2)

third_std_start = mean - (std*3)
third_std_end = mean + (std*3)


list_of_data_1std = [results for results in result if results>first_std_start and results<first_std_end] 
print("{}%of data lies between 1 standard deviation".format(len(list_of_data_1std)*100.0/len(result)))

list_of_data_2std = [results for results in result if results>second_std_start and results<second_std_end]
print("{}%of data lies between 2 standard deviation".format(len(list_of_data_2std)*100.0/len(result)))

list_of_data_3std = [results for results in result if results>third_std_start and results<third_std_end]
print("{}%of data lies between 3 standard deviation".format(len(list_of_data_3std)*100.0/len(result)))