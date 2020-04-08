# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 15:56:13 2020

@author: thinkpad
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir(r'D:\Gitkraken\IBI1_2019-20\Practical7')

covid_data = pd.read_csv("full_data.csv")
# Part 2
n = covid_data.iloc[0:15:3,:]
print(n)
# Part 3
df = pd.DataFrame(covid_data)
f = [0 for i in range(len(df))]
for i in range(len(df)):
    if covid_data.iloc[i,1] == 'Afghanistan':
        f[i] = True
    else:
        f[i] = False
print(f)
#Prepare for part 4:6 
world_dates = []
world_new_cases = []
world_new_deaths = []
for i in range(len(df)):
    if covid_data.iloc[i,1] == 'World':
        world_new_cases.append (covid_data.iloc[i,2])
        world_dates.append (covid_data.iloc[i,0])
        world_new_deaths.append(covid_data.iloc[i,3])
# Part 4
world_mean = np.mean(world_new_cases)
world_median = np.median (world_new_cases)
print (world_mean)
print (world_median)
# Part 5
plt.boxplot(world_new_cases,
            showcaps = 'world new cases',
            vert = True,
            meanline = True,
            whis = 1.5,
            patch_artist = True,
            showbox = True,
            notch = False)
plt.show()
# Part 6
plt.plot(world_dates, world_new_cases, 'b+')
plt.xticks(world_dates[0:len(world_dates):4],rotation=-90)
plt.show()
plt.plot(world_dates, world_new_deaths, 'b+')
plt.xticks(world_dates[0:len(world_dates):4],rotation=-90)
plt.show()

# Question
China_dates = []
China_new_cases = []
China_total_cases = []
for i in range(len(df)):
    if covid_data.iloc[i,1] == 'China':
        China_dates.append (covid_data.iloc[i,0])
        China_new_cases.append (covid_data.iloc[i,2])
        China_total_cases.append(covid_data.iloc[i,4])
plt.boxplot(China_new_cases,
            showcaps = 'world new cases',
            vert = True,
            meanline = True,
            whis = 1.5,
            patch_artist = True,
            showbox = True,
            notch = False)
plt.show()
plt.plot(China_dates, China_new_cases, 'b+')
plt.xticks(China_dates[0:len(world_dates):6],rotation=-90)
plt.show()
plt.plot(China_dates, China_total_cases, 'b+')
plt.xticks(China_dates[0:len(world_dates):6],rotation=-90)
plt.show()