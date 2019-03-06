import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt
import descartes
import plotly 
plotly.tools.set_credentials_file(username='smj46', api_key='nniqvcTGdUFaIgIuXXqW')
import plotly.plotly as py
import plotly.graph_objs as go
import geopandas as gpd
from shapely.geometry import Point, Polygon
from matplotlib.ticker import MaxNLocator

###Graph resolution maps###

#First plot

area=gpd.read_file(r'C:\Users\smj46\Desktop\Python Scripts\Shapefiles\77_4\Subcatchments.shp')
fig, ax = plt.subplots(nrows=1, ncols=4, figsize=(15,15))
area.plot(ax=ax[0], color='green', alpha=.75)
line=gpd.read_file(r'C:\Users\smj46\Desktop\Python Scripts\Shapefiles\77_4\Conduits.shp')
line.plot(ax=ax[0])
point=gpd.read_file(r'C:\Users\smj46\Desktop\Python Scripts\Shapefiles\77_4\Junctions.shp')
point.plot(ax=ax[0])

#Second plot

area=gpd.read_file(r'C:\Users\smj46\Desktop\Python Scripts\Shapefiles\77_3\Subcatchments.shp')
area.plot(ax=ax[1], color='green', alpha=.75)
line=gpd.read_file(r'C:\Users\smj46\Desktop\Python Scripts\Shapefiles\77_3\Conduits.shp')
line.plot(ax=ax[1])
point=gpd.read_file(r'C:\Users\smj46\Desktop\Python Scripts\Shapefiles\77_3\Junctions.shp')
point.plot(ax=ax[1])

#Third plot

area=gpd.read_file(r'C:\Users\smj46\Desktop\Python Scripts\Shapefiles\77_2\Subcatchments.shp')
area.plot(ax=ax[2], color='green', alpha=.75)
line=gpd.read_file(r'C:\Users\smj46\Desktop\Python Scripts\Shapefiles\77_2\Conduits.shp')
line.plot(ax=ax[2])
point=gpd.read_file(r'C:\Users\smj46\Desktop\Python Scripts\Shapefiles\77_2\Junctions.shp')
point.plot(ax=ax[2])

#Fourth plot

area=gpd.read_file(r'C:\Users\smj46\Desktop\Python Scripts\Shapefiles\77_1\Subcatchments.shp')
area.plot(ax=ax[3], color='green', alpha=.75)
line=gpd.read_file(r'C:\Users\smj46\Desktop\Python Scripts\Shapefiles\77_1\Conduits.shp')
line.plot(ax=ax[3])
point=gpd.read_file(r'C:\Users\smj46\Desktop\Python Scripts\Shapefiles\77_1\Junctions.shp')
point.plot(ax=ax[3])

#Formatting
ax[0].axes.get_xaxis().set_visible(False)
ax[0].axes.get_yaxis().set_visible(False)
ax[1].axes.get_xaxis().set_visible(False)
ax[1].axes.get_yaxis().set_visible(False)
ax[2].axes.get_xaxis().set_visible(False)
ax[2].axes.get_yaxis().set_visible(False)
ax[3].axes.get_xaxis().set_visible(False)
ax[3].axes.get_yaxis().set_visible(False)


###Model simulation results###

#Import Data
data=pd.read_csv(r'C:\Users\smj46\Desktop\Python Scripts\Event3_scales.csv')
One=data.loc[:,"One"]
Two=data.loc[:,"Two"]
Three=data.loc[:,"Three"]
Four=data.loc[:,"Four"]
Rainfall=data.loc[:,"Rainfall"]
Date=data.loc[:,"Date"]
Obs=data.loc[:,"Observed"]

#Plot
fig,ax = plt.subplots(figsize=(20,10))
ax.plot(Date,One)
ax.plot(Date,Two)
ax.plot(Date,Three)
ax.plot(Date,Four)
ax.plot(Date,Obs,marker='o')
ax.set_ylabel('Runoff (m3/s)')
ax.legend()
plt.xticks(rotation=45)
ax.xaxis.set_major_locator(MaxNLocator(4))

#Formatting
plt.title('Resolution Comparison')

SMALL_SIZE = 20
MEDIUM_SIZE = 20
BIGGER_SIZE = 20

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

#Secondary Axis
ax2=ax.twinx()
ax2.bar(Date,Rainfall, alpha=.1)
plt.gca().invert_yaxis()
ax2.set_ylabel('Rainfall (mm/hr)')
plt.ylim([10,0])
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.xticks(rotation=45)
ax2.xaxis.set_major_locator(MaxNLocator(4))

#Data Analysis
NSE1=round(1-(sum((One-Obs)**2)/(sum(Obs-np.mean(Obs)**2))),2)
NSE2=round(1-(sum((Two-Obs)**2)/(sum(Obs-np.mean(Obs)**2))),2)
NSE3=round(1-(sum((Three-Obs)**2)/(sum(Obs-np.mean(Obs)**2))),2)
NSE4=round(1-(sum((Four-Obs)**2)/(sum(Obs-np.mean(Obs)**2))),2)
max1=round(max(One),2)
max2=round(max(Two),2)
max3=round(max(Three),2)
max4=round(max(Four),2)
maxo=round(max(Obs),2)
vol1=round(sum(One)*5*60,0)
vol2=round(sum(Two)*5*60,0)
vol3=round(sum(Three)*5*60,0)
vol4=round(sum(Four)*5*60,0)
volo=round(sum(Obs)*5*60,0)

#Table Display
tabledata = go.Table(
    header=dict(values=[' ', '1st Order', '2nd Order', '3rd Order', '4th Order', 'Observed']),
    cells=dict(values=[['Total Volume (m3)', 'Max Flow (m3/s)', 'NSE'],
                       [vol1, max1, NSE1],
                       [vol2, max2, NSE2],
                       [vol3, max3, NSE3],
                       [vol4, max4, NSE4],
                       [volo, maxo, '-']]))

data = [tabledata] 
py.iplot(data, filename = 'basic_table')
