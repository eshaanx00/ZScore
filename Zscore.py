import plotly.figure_factory as px
import plotly.graph_objects as gx
import pandas as pd
import statistics
import random

Data =  pd.read_csv('medium_data.csv')
list = Data["reading_time"].tolist()

def sampleTime(counter):
    marks=[]
    for i in range(0,counter):
        randomInt = random.randint(0,len(list)-1)
        value = list[randomInt]
        marks.append(value)
    mean = statistics.mean(marks)
    return mean

list1=[]
for i in range(1000):
    sampleData = sampleTime(100)
    list1.append(sampleData)


mean = statistics.mean(list1)
deviation = statistics.stdev(list1)

time_first_sd_start,time_first_sd_end = mean-deviation,deviation+mean
time_second_sd_start,time_second_sd_end = mean-(deviation*2),(deviation*2)+mean
time_third_sd_start,time_third_sd_end = mean-(deviation*3),(deviation*3)+mean

fig = px.create_distplot([list1],["result"],show_hist=False)
fig.add_trace(gx.Scatter(x=[mean,mean],y=[0,1.2],mode='lines',name='mean'))
fig.add_trace(gx.Scatter(x=[time_first_sd_start,time_first_sd_start],y=[0,1.2],mode='lines',name='sd1'))
fig.add_trace(gx.Scatter(x=[time_first_sd_end,time_first_sd_end],y=[0,1.2],mode='lines',name='sd1'))

fig.add_trace(gx.Scatter(x=[time_second_sd_start,time_second_sd_start],y=[0,1.2],mode='lines',name='sd2'))
fig.add_trace(gx.Scatter(x=[time_second_sd_end,time_second_sd_end],y=[0,1.2],mode='lines',name='sd2'))

fig.add_trace(gx.Scatter(x=[time_third_sd_start,time_third_sd_start],y=[0,1.2],mode='lines',name='sd3'))
fig.add_trace(gx.Scatter(x=[time_third_sd_end,time_third_sd_end],y=[0,1.2],mode='lines',name='sd3'))

fig.show()

data1 = sampleTime(30)

#mean_math_score_1 = statistics.mean(data1)
#print(mean_math_score_1)

fig1 = px.create_distplot([list1],["result"],show_hist=False)
fig1.add_trace(gx.Scatter(x=[mean,mean],y=[0,1.2],mode='lines',name='mean'))
fig1.add_trace(gx.Scatter(x=[data1,data1],y=[0,1.2],mode='lines',name='mean of sample1'))
fig1.add_trace(gx.Scatter(x=[time_first_sd_end,time_first_sd_end],y=[0,1.2],mode='lines',name='sd1'))

fig1.show()

data2 = sampleTime(30)

#mean_math_score_2 = statistics.mean(data2)
#print(mean_math_score_2)

fig2 = px.create_distplot([list1],["result"],show_hist=False)
fig2.add_trace(gx.Scatter(x=[mean,mean],y=[0,1.2],mode='lines',name='mean'))
fig2.add_trace(gx.Scatter(x=[data2,data2],y=[0,1.2],mode='lines',name='mean of sample2'))
fig2.add_trace(gx.Scatter(x=[time_second_sd_end,time_second_sd_end],y=[0,1.2],mode='lines',name='sd2'))

fig2.show()

data3 = sampleTime(30)
#mean_math_score_3 = statistics.mean(data3)
#print(mean_math_score_3)

fig3 = px.create_distplot([list1],["result"],show_hist=False)
fig3.add_trace(gx.Scatter(x=[mean,mean],y=[0,1.2],mode='lines',name='mean'))
fig3.add_trace(gx.Scatter(x=[data3,data3],y=[0,1.2],mode='lines',name='mean of sample3'))
fig3.add_trace(gx.Scatter(x=[time_third_sd_end,time_third_sd_end],y=[0,1.2],mode='lines',name='sd3'))

fig3.show()

z_score_1 = (data1-mean)/deviation
print("Z Score 1",z_score_1)

z_score_2 = (data2-mean)/deviation
print("Z Score 2",z_score_2)

z_score_3 = (data3-mean)/deviation
print("Z Score 3",z_score_3)