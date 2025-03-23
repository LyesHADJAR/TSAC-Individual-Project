import pandas as pd

# Read the CSV file
df = pd.read_csv('/home/lyes/Desktop/3Y/This Year /S6/Time Series /TSAC-Individual-Project/data/Algiers_Weather_Data.csv')

# Select only the 'time' and 'temperature_2m_mean (°C)' columns
df_filtered = df[['time', 'temperature_2m_mean (°C)']]

# Save the filtered data to a new CSV file
output_path = '/home/lyes/Desktop/3Y/This Year /S6/Time Series /TSAC-Individual-Project/data/algiers_temp.csv'
df_filtered.to_csv(output_path, index=False)

print(f"Data has been filtered and saved to {output_path}")