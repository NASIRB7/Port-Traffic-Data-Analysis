# Import necessary libraries
import numpy as np 
import pandas as pd 
from IPython.display import display
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('/kaggle/input/port-traffic-q3-2023/Port traffic Q3 2023.CSV')

# Display the first 10 rows of the DataFrame
df.head(10)

# Convert the 'التاريخ' column to datetime format
df['التاريخ'] = pd.to_datetime(df['التاريخ'])

# Define start and end dates for filtering
start_date = '2023-01-01'
end_date = '2024-01-01'

# Filter DataFrame based on date range
filtered_df = df[(df['التاريخ'] >= start_date) & (df['التاريخ'] <= end_date)]

# Further filter for movements greater than 200
filtered_df_greater_than_200 = filtered_df[filtered_df['عدد الحركات'] > 200]

# Display the filtered DataFrame
display(filtered_df_greater_than_200)

# Calculate and display daily traffic
daily_traffic = df.groupby('التاريخ')['عدد الحركات'].sum()
most_active_day = daily_traffic.idxmax()
max_traffic_day_count = daily_traffic.max()
display(f"The most active day is {most_active_day.strftime('%Y-%m-%d')} with {max_traffic_day_count} movements.")

# Convert 'الساعة' column to hour format
df['الساعة'] = pd.to_datetime(df['الساعة'], format='%H').dt.hour

# Calculate and display hourly traffic
hourly_traffic = df.groupby('الساعة')['عدد الحركات'].sum()
display(hourly_traffic)

# Find the most active hour
most_active_hour = hourly_traffic.idxmax()

# Extract records for the most active day and hour
most_active_record = df[(df['التاريخ'] == most_active_day.strftime('%Y-%m-%d')) & (df['الساعة'] == most_active_hour)]

# Display information for the most active day and hour
print(f"Information for the most active day ({most_active_day.strftime('%Y-%m-%d')}) and hour ({most_active_hour}):")
display(most_active_record)

# Plot the number of movements over time
plt.figure(figsize=(10, 6))
filtered_df.groupby('التاريخ')['عدد الحركات'].sum().plot(kind='line', marker='o', linestyle='-')
plt.title('Number of Movements Over Time')
plt.xlabel('الايام')
plt.ylabel('Number of Movements')
plt.grid(True)
plt.show()
