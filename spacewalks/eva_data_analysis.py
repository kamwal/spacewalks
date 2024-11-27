import json
import csv
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd

# https://data.nasa.gov/resource/eva.json (with modifications)
input_file = open('eva-data.json', 'r')
output_file = open('eva-data.csv','w')
graph_file = 'cumulative_eva_grapth.png'

fieldnames = ("EVA #", "Country", "Crew    ", "Vehicle", "Date", "Duration", "Purpose")

#data_file = []

print("--START--")
print(f'Reading JSON file {input_file}')
# Read the data from a JSON file into a Pandas dataframe
eva_df = pd.read_json(input_file, convert_dates=['date'])
eva_df['eva'] = eva_df['eva'].astype(float)
# Clean the data by removing any incomplete rows and sort by date
eva_df.dropna(axis=0, inplace=True)
eva_df.sort_values('date', inplace=True)

'''
w=csv.writer(output_file)
'''
print(f'Saving to CSV file {output_file}')
# Save dataframe to CSV file for later analysis
eva_df.to_csv(output_file, index=False)

time = []
date =[]

print(f'Plotting cumulative spacewalk duration and saving to {graph_file}')
# Plot cumulative time spent in space over years
eva_df['duration_hours'] = eva_df['duration'].str.split(":").apply(lambda x: int(x[0]) + int(x[1])/60)
eva_df['cumulative_time'] = eva_df['duration_hours'].cumsum()
plt.plot(eva_df['date'], eva_df['cumulative_time'], 'ko-')
plt.xlabel('Year')
plt.ylabel('Total time spent in space to date (hours)')
plt.tight_layout()
plt.savefig(graph_file)
plt.show()
print("--END--")