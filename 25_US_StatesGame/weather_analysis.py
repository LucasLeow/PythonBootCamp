import pandas as pd

df = pd.read_csv('weather_data.csv')
print(df[df['day'] == 'Monday'])
print(df[df['temp'] == df['temp'].max()])