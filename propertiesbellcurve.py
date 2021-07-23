import random
import statistics
import plotly.figure_factory as ff
import pandas as pd
import csv

df=pd.read_csv("weight.csv")
height_list=df["Height(Inches)"].to_list()
weight_list=df["Weight(Pounds)"].to_list()
height_mean=statistics.mean(height_list)
weight_mean=statistics.mean(weight_list)
height_median=statistics.median(height_list)
weight_median=statistics.median(weight_list)
height_mode=statistics.mode(height_list)
weight_mode=statistics.mode(weight_list)

print("mean, median, and mode of height is {},{},{} respectively".format(height_mean,height_median,height_mode) )
print("mean, median, and mode of height is {},{},{} respectively".format(weight_mean,weight_median,weight_mode) )
height_first_std_deviation_start,height_first_std_deviation_end=height_mean-height_std_deviation,height_mean+height_std_deviation
height_second_std_deviation_start,height_second_std_deviation_end=height_mean-(2*height_std_deviation),height_mean+(2*height_std_deviation)
height_third_std_deviation_start,height_third_std_deviation_end=height_mean-(3*height_std_deviation),height_mean+(3*height_std_deviation)



weight_first_std_deviation_start,weight_first_std_deviation_end=weight_mean-weight_std_deviation,weight_mean+weight_std_deviation
weight_second_std_deviation_start,weight_second_std_deviation_end=weight_mean-(2*weight_std_deviation),weight_mean+(2*weight_std_deviation)
weight_third_std_deviation_start,weight_third_std_deviation_end=weight_mean-(3*weight_std_deviation),weight_mean+(3*weight_std_deviation)


height_list_of_data_within_1_std_deviation = [result for result in height_list if result > height_first_std_deviation_start and result < height_first_std_deviation_end]
height_list_of_data_within_2_std_deviation = [result for result in height_list if result > height_second_std_deviation_start and result < height_second_std_deviation_end]
height_list_of_data_within_3_std_deviation = [result for result in height_list if result > height_third_std_deviation_start and result < height_third_std_deviation_end]

weight_list_of_data_within_1_std_deviation = [result for result in weight_list if result > weight_first_std_deviation_start and result < weight_first_std_deviation_end]
weight_list_of_data_within_2_std_deviation = [result for result in weight_list if result > weight_second_std_deviation_start and result < weight_second_std_deviation_end]
weight_list_of_data_within_3_std_deviation = [result for result in weight_list if result > weight_third_std_deviation_start and result < weight_third_std_deviation_end]

print("{}% of height lies within 1 standard deviation".format(len(height_list_of_data_within_1_standard_deviation)*100.0/len(height_list)))
print("{}% of height lies within 2 standard deviation".format(len(height_list_of_data_within_2_standard_deviation)*100.0/len(height_list)))
print("{}% of height lies within 3 standard deviation".format(len(height_list_of_data_within_3_standard_deviation)*100.0/len(height_list)))
print("{}% of weight lies within 1 standard deviation".format(len(weight_list_of_data_within_1_standard_deviation)*100.0/len(weight_list)))
print("{}% of weight lies within 2 standard deviation".format(len(weight_list_of_data_within_2_standard_deviation)*100.0/len(weight_list)))
print("{}% of weight lies within 3 standard deviation".format(len(weight_list_of_data_within_3_standard_deviation)*100.0/len(weight_list)))



dice_result=[]
for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice_result.append(dice1+dice2)

mean=sum(dice_result)/len(dice_result)
standard_deviation=statistics.stdev(dice_result)

#print(mean)
#print(standard_deviation)


    
median=statistics.median(dice_result)
mode=statistics.mode(dice_result)
#print(median)
#print(mode)

graph=ff.create_distplot([dice_result],["results"],show_hist=False)
graph.show()

first_standard_deviation_start,first_standard_deviation_end=mean-standard_deviation,mean+standard_deviation
second_standard_deviation_start,second_standard_deviation_end=mean-(2*standard_deviation)+mean+(2*standard_deviation)
print("{}% of data lies within one standard deviation".format(len(list_of_data_within_one_standard_deviation)*100.0/len(dice_result)))
